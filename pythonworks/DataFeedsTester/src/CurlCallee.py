import logging, re, os, fnmatch, requests

from requests   import exceptions

from FileConstants import FileConstants
from HTTPConstants import HTTPConstants


def main():
    try:
        calleeObj = CurlCallee()
        calleeObj.execute()
    except KeyboardInterrupt:
        logging.info("Program exited by user")

class CurlCallee:
    fileConstants = FileConstants()
    httpConstants = HTTPConstants()
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    urls = dict()
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
                for file in self.fileConstants.feedDictionary.get(key):
                    result = self.findFile(file, os.path.pardir)
                    if result:
                        file = result[0]
                    else:
                        logging.error("Didn't find feed file for " + key)
                    print("Gathering URLs from " + file + " of type " + key)
                    with open(file,'r') as fileName:
                        lines = fileName.read().splitlines()
                        for line in lines:
                            lineUrls = re.findall(r'(?:http|https|www)(?:[^\\\]"<>]*)', line)
                            #lineUrls = re.findall(r'(https?://\S+)', line)
                            urls[key].append(lineUrls)
        except FileNotFoundError:
            logging.error("Check the file names in FileConstants file")
        except UnicodeDecodeError:
            logging.error("Make sure that the file is in UTF-8 format " + file)


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
        except (requests.exceptions.ConnectionError, ConnectionError):
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
    def execute(self):
        self.gatherUrls(self.urls)
        self.testUrls(self.urls)