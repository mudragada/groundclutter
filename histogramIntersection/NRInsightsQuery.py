import requests, logging, urllib, json
from requests import exceptions

class NRInsightsQuery:
    def __init__(self):
        with open('config.json', 'r') as json_data_file:
            self.config = json.load(json_data_file)
    def queryInsights(self, query):
        nrUrl = self.config['NRInsightsAPIUrl']
        try:
            print(query)
            if query:
				nrUrl += urllib.quote(query)
            headers = {'content-type': 'application/json', 'X-Query-Key': self.config['X-Query-Key']}
            curlResponse = requests.get(nrUrl, headers=headers, timeout=5)
            return curlResponse
        except (requests.exceptions.ConnectionError):
            logging.error("ERROR:: Connection issues on " + socket)
            return None

    def getBackendDurationQuery(self, FromDate, ToDate):
        query = "SELECT histogram(backendDuration, " + str(self.config['maxBackendDuration']) + ", " + str(self.config['histogramBins']) + ") FROM PageView WHERE appName = 'AWP WebUI - ProdWD'" + " SINCE " + FromDate + " UNTIL " + ToDate
        return query

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