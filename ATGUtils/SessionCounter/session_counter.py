import requests, logging, sys, getpass, re
from requests import exceptions
from requests.auth import HTTPBasicAuth
from lxml import etree
from io import StringIO
from lxml.html import fromstring

class DynAdminConstants:
    instancesFile = 'instances'
    instancesFileLocation = '/flush'
    basePath = '/dyn/admin/nucleus/'
    def __init__(self):
        self.dynUserName = raw_input("Enter your username:")
        self.dynPassword = getpass.getpass(prompt='Password:', stream=None)
        self.componentPath = raw_input("Enter your component path:")
        self.componentPropertyName = raw_input("Enter the propertyName:")


class HTTPConstants:
    responseCodeDictionary = {  '100'   :   'CONTINUE',
                                '101'   :   'SWITCHING_PROTOCOLS',
                                '102'   :   'PROCESSING',
                                '200'   :   'OK',
                                '201'   :   'CREATED',
                                '202'   :   'ACCEPTED',
                                '203'   :   'NON_AUTHORITATIVE_INFORMATION',
                                '204'   :   'NO_CONTENT',
                                '205'   :   'RESET_CONTENT',
                                '206'   :   'PARTIAL_CONTENT',
                                '207'   :   'MULTI_STATUS',
                                '226'   :   'IM_USED',
                                '300'   :   'MULTIPLE_CHOICES',
                                '301'   :   'MOVED_PERMANENTLY',
                                '302'   :   'FOUND',
                                '303'   :   'SEE_OTHER',
                                '304'   :   'NOT_MODIFIED',
                                '305'   :   'USE_PROXY',
                                '307'   :   'TEMPORARY_REDIRECT',
                                '400'   :   'BAD_REQUEST',
                                '401'   :   'UNAUTHORIZED',
                                '402'   :   'PAYMENT_REQUIRED',
                                '403'   :   'NOT_FOUND',
                                '404'   :   'PAGE_NOT_FOUND',
                                '405'   :   'METHOD_NOT_ALLOWED',
                                '406'   :   'NOT_ACCEPTABLE',
                                '407'   :   'PROXY_AUTHENTICATION_REQUIRED',
                                '408'   :   'REQUEST_TIMEOUT',
                                '409'   :   'CONFLICT',
                                '410'   :   'GONE',
                                '411'   :   'LENGTH_REQUIRED',
                                '412'   :   'PRECONDITION_FAILED',
                                '413'   :   'REQUEST_ENTITY_TOO_LARGE',
                                '414'   :   'REQUEST_URI_TOO_LONG',
                                '415'   :   'UNSUPPORTED_MEDIA_TYPE',
                                '416'   :   'REQUESTED_RANGE_NOT_SATISFIABLE',
                                '417'   :   'EXPECTATION_FAILED',
                                '422'   :   'UNPROCESSABLE_ENTITY',
                                '423'   :   'LOCKED',
                                '424'   :   'FAILED_DEPENDENCY',
                                '426'   :   'UPGRADE_REQUIRED',
                                '500'   :   'INTERNAL_SERVER_ERROR',
                                '501'   :   'NOT_IMPLEMENTED',
                                '502'   :   'BAD_GATEWAY',
                                '503'   :   'SERVICE_UNAVAILABLE',
                                '504'   :   'GATEWAY_TIMEOUT',
                                '505'   :   'HTTP_VERSION_NOT_SUPPORTED',
                                '507'   :   'INSUFFICIENT_STORAGE',
                                '510'   :   'NOT_EXTENDED'
    }



class SessionCounter:
    def __init__(self):
        self.constants = DynAdminConstants()
        self.httpConstants = HTTPConstants()
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger("requests").setLevel(logging.WARNING)


    def curlOnAllSocketsFromFile(self):
        try:
            with open(self.constants.instancesFile,'r') as fileName:
                lines = fileName.read().splitlines()
                for line in lines:
                    if(re.match('.{5,15}\:832\d', line)):
                        curlResponse = self.sendCurlRequest(line, True, True, True)
                        responseCode = self.validCurlResponseCode(curlResponse)
                        if ( responseCode == 'OK'):
                            value = self.parseHTMLForSessionCount(curlResponse)
                            logging.info(line + " - " + value)
                        elif(responseCode == 'UNAUTHORIZED'):
                            logging.info("Invalid Dyn Admin credentials. Check again, exiting..")
                            sys.exit(-1)
                        else:
                            logging.info(line + " - " + "ERROR")
        except (IOError):
            logging.error("Didn't find the file " + self.constants.instancesFile)

    def sendCurlRequest(self,socket, hasComponentPath, hasBasePath, hasPropertyName):
        dyn_admin_url = 'http://' + socket
        if(hasBasePath):
            dyn_admin_url += self.constants.basePath
        if(hasComponentPath):
            dyn_admin_url += self.constants.componentPath
        if(hasPropertyName):
            dyn_admin_url += '?propertyName=' + self.constants.componentPropertyName
        try:
            curlResponse = requests.get(dyn_admin_url, auth=HTTPBasicAuth(self.constants.dynUserName, self.constants.dynPassword ), timeout=5)
            return curlResponse
        except (requests.exceptions.ConnectionError):
            logging.error("ERROR:: Connection issues on " + socket)
            return None

    def validCurlResponseCode(self, curlResponse):
        try:
            status_code = curlResponse.status_code
            if(str(status_code) in self.httpConstants.responseCodeDictionary.keys()):
                return self.httpConstants.responseCodeDictionary.get(str(status_code))
            else:
                return 'UNKNOWN'
        except AttributeError:
            logging.error("ERROR::Curl Response doesn't have attributes")

    def parseHTMLForSessionCount(self, curlResponse):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(curlResponse.text), parser)
        form_tree = fromstring(etree.tostring(tree.getroot()))
        return ([e.text_content() for e in form_tree.xpath('//span')][0])


def main():
    sessionCounter = SessionCounter()
    sessionCounter.curlOnAllSocketsFromFile()


sys.exit(main())


