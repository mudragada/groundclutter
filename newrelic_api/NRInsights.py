## NRInsights.py

import requests, logging, urllib, json
from requests import exceptions
from main import config, requestObj, 

class NRInsights:
	
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
