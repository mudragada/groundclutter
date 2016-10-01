import logging, re, os, fnmatch, requests, socket, gzip, shutil, paramiko, mimetypes

from Constants import FileConstants
from Constants import HTTPConstants

## static main method
def main():
    try:
        calleeObj = CurlCallee()
        calleeObj.execute()
    except KeyboardInterrupt:
        logging.info("Program exited by user")


def setLoggingPrefs():
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger("requests").setLevel(logging.WARNING)


class CurlCallee:
    fileConstants = FileConstants()
    httpConstants = HTTPConstants()

    urls = dict()
    setLoggingPrefs()


    def findFile(self, pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result


    def gatherUrls(self, urls):
        try:
            for key in self.fileConstants.feedDictionary:
                urls[key] = []
                for filepattern in self.fileConstants.feedDictionary.get(key):
                    result = self.findFile(filepattern, os.path.pardir)
                    if result:
                        file = result[0]
                    else:
                        logging.error("Didn't find feed file for " + key)
                    logging.info("Gathering URLs from " + file + " of type " + key)
                    if("gzip" not in self.determineFileType(file)):
                        with open(file,'r') as fileName:
                            self.readUrlsFromFile(fileName, urls, key)
                    else:
                        with gzip.open(file, 'rb') as fileName:
                            self.readUrlsFromFile(fileName, urls, key)

        except IOError:
            logging.error("Check the file names in FileConstants file")
        except UnicodeDecodeError:
            logging.error("Make sure that the file is in UTF-8 format " + file)

    def readUrlsFromFile(self, fileName, urls, key):
        lines = fileName.read().splitlines()
        for line in lines:
            lineUrls = re.findall(r'(?:http|https|www)(?:[^\\\]"<>]*)', line)

            ## replace http: with https:
            lineUrls = [url.replace('http:', 'https:') for url in lineUrls]
            urls[key].append(lineUrls)

    def printUrls(self, urls):
        counter = 0
        for key in urls:
            for value in urls.get(key):
                if isinstance(value, list):
                    for innerValue in value:
                        counter += 1
                        logging.info (str(counter) + ". " + innerValue +  " \n")
                else:
                    counter += 1
                    logging.info (str(counter) + ". " + value +  " \n")


    def testUrls(self, urls):
        counter = 0
        for key in urls:
            for value in urls.get(key):
                if isinstance(value, list):
                    for innerValue in value:
                        counter += 1
                        curlResponse = self.sendCurlRequest(innerValue)
                        logging.info(str(counter) + ". " + innerValue + " : " + str(curlResponse) )
                else:
                    counter += 1
                    responseCode = self.sendCurlRequest(value)
                    if(responseCode == 'OK'):
                        logging.info(str(counter) + ". " + value + " : " + responseCode )
                    else:
                        logging.warning(str(counter) + ". " + value + " : " + responseCode)


    def sendCurlRequest(self,site_url):
        try:
            curlResponse = requests.get(site_url, timeout=10)
            return self.processedCurlResponse(curlResponse)
        except (requests.exceptions.InvalidSchema):
            return 'INVALID URL'
        except (requests.exceptions.ConnectionError):
            return 'CONNECTION ERROR'
        except (requests.exceptions.ReadTimeout):
            return 'READTIMEOUT ERROR'
        except (AttributeError):
            return 'ATTRIBUTE ERROR'
        except (requests.exceptions.TooManyRedirects):
            return 'TOO MANY REDIRECTS'

    def processedCurlResponse(self, curlResponse):
        status_code = str(curlResponse.status_code)
        curl_history = curlResponse.history
        respCodeDict = self.httpConstants.responseCodeDictionary
        if not curl_history:
            # If the curl response doesn't have a history, return the status code
            if (str(status_code) in respCodeDict.keys()):
                return respCodeDict.get(str(status_code))
            else:
                return 'UNKNOWN'
        else:
            # curl response has a history - return the first of the response codes
            for curlHistResponse in curl_history:
                if(str(curlHistResponse.status_code) in respCodeDict.keys()):
                    return respCodeDict.get(str(curlHistResponse.status_code))
                else:
                    # if none of the response codes are matching, return the original status_code itself
                    return respCodeDict.get(status_code)

    def gatherFiles(self):
        if(socket.gethostname().startswith(self.fileConstants.statsHost)):
            self.findAndCopyLocalMatchingFiles()
        else:
            self.findAndCopyRemoteMatchingFiles()



    def findAndCopyLocalMatchingFiles(self):
        logging.info("You're already on " + self.fileConstants.statsHost +", skipping the scp and doing a cp")
        searchFileResultsDict = dict()
        ## Fill the searchFileResultsDict with the matching file pattern for each feedtype
        for key in self.fileConstants.feedDictionary:
            for filepattern in self.fileConstants.feedDictionary.get(key):
                searchFileResultsDict.clear()
                os.chdir(self.fileConstants.feedFilesLocation)
                for file in os.listdir('.'):
                    if (fnmatch.fnmatch(file, filepattern)):
                        searchFileResultsDict[file] = os.lstat(file).st_mtime

                fileToDownload = max(searchFileResultsDict, key=searchFileResultsDict.get)
                shutil.copyfile(self.fileConstants.feedFilesLocation + fileToDownload, fileToDownload)


    def findAndCopyRemoteMatchingFiles(self):
        logging.info("Sftp'ing the feeds from " + self.fileConstants.feedFilesLocation + " from " + self.fileConstants.statsHost)
        try:
            sshClient = paramiko.SSHClient()
            sshClient.load_system_host_keys()
            sshClient.connect(self.fileConstants.statsHost)
            ## 1. Open a new SFTP server on the SSH Connection
            sftpClient = sshClient.open_sftp()
            sftpClient.chdir(self.fileConstants.feedFilesLocation)
            searchFileResultsDict = dict()
            ## 2. Fill the searchFileResultsDict with the matching file pattern for each feedtype
            for key in self.fileConstants.feedDictionary:
                for filepattern in self.fileConstants.feedDictionary.get(key):
                    searchFileResultsDict.clear()
                    for file in sftpClient.listdir():
                        if (fnmatch.fnmatch(file, filepattern)):
                            searchFileResultsDict[file] = sftpClient.lstat(file).st_mtime

            ## 3. find the file with the latest timestamp
                    fileToDownload = max(searchFileResultsDict, key=searchFileResultsDict.get)
                    logging.info("Downloading " + fileToDownload)
            ## 4. Download the latest file
                    sftpClient.get(fileToDownload, fileToDownload)

            sshClient.close()
            sftpClient.close()
        except (TypeError, paramiko.SSHException, IOError, AttributeError):
            sftpClient.close()
            sshClient.close()

    def cleanFiles(self):
        os.chdir('.')
        for key in self.fileConstants.feedDictionary:
            for filepattern in self.fileConstants.feedDictionary.get(key):
                for file in os.listdir('.'):
                    if (fnmatch.fnmatch(file, filepattern)):
                        logging.info("Removing " + file)
                        os.remove(file)

    def determineFileType(self, filename):
        type = mimetypes.guess_type(filename)
        return type

    def execute(self):
        self.gatherFiles()
        self.gatherUrls(self.urls)
        #self.printUrls(self.urls)
        self.testUrls(self.urls)
        self.cleanFiles()