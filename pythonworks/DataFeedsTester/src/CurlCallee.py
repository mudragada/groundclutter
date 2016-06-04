import logging
import re

import requests
from requests                       import exceptions

from DataFeedsTester.src import FileConstants
from Curls.Curls.HTTPConstants import HTTPConstants


def main():
    calleeObj = CurlCallee()
    calleeObj.execute()

class CurlCallee:
    fileConstants = FileConstants()
    httpConstants = HTTPConstants()
    urls = dict()
    def gatherUrls(self, urls):
        for key in self.fileConstants.feedDictionary:
            print (key, self.fileConstants.feedDictionary.get(key))
            urls[key] = []
            for file in self.fileConstants.feedDictionary.get(key):
                with open(file,'r') as fileName:
                    lines = fileName.read().splitlines()
                    for line in lines:
                        lineUrls = re.findall(r'(https?://\S+)', line)
                        urls[key].append(lineUrls)

        #self.printUrls(urls)
        return None

    def printUrls(self, urls):
        counter = 0
        for key in urls:
            for value in urls.get(key):
                if isinstance(value, list):
                    for innerValue in value:
                        counter += 1
                        print (str(counter) + ". type - " + key + " URL - " + innerValue + "\n")
                else:
                    counter += 1
                    print (str(counter) + ". type - " + key + " URL - " + value +  " \n")
    def testUrls(self, urls):
        counter = 0
        for key in urls:
            for value in urls.get(key):
                if isinstance(value, list):
                    for innerValue in value:
                        counter += 1
                        curlResponse = self.sendCurlRequest(innerValue)
                        print(str(counter) + " URL - " + innerValue + " : " + str(curlResponse) )
                else:
                    counter += 1
                    responseCode = self.sendCurlRequest(value)
                    if(responseCode == 'OK'):
                        logging.info(str(counter) + " URL - " + value + " : " + responseCode )
                    else:
                        logging.error(str(counter) + " URL - " + value + " : " + responseCode)

                    # print (str(counter) + ". type - " + key + " URL - " + value +  " \n")
    def sendCurlRequest(self,site_url):
        try:
            curlResponse = requests.get(site_url, timeout=10)
            return self.processedCurlResponse(curlResponse)
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