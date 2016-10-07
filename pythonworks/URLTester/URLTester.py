__author__ = 'Krishna Mudragada    '

import requests, requests.exceptions
class URLTester:

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

