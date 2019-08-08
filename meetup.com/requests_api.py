# requests_api.py

import requests, json
from datetime import datetime as dt

def log(msg):
	print ('[%s]: %s' % (dt.now().isoformat(), msg))

class requestsApi:
	def GET_json(self,url, parameters):
	# Issues a GET request. params should be a dict and will get urlencoded
	# and appened as a query string.
		try:
			if url:
				log('[API GET] - ' + url)
				headers = {'content-type': 'application/json'}
				response = requests.get(url, headers=headers, params=parameters,timeout=5)
				# log(json.dumps(response.json()))
				## TO DO 200 OK vs 429 Too Many Requests
				return response.json()
		except(requests.exceptions.ConnectionError):
			log("ERROR:: Connection issues")
			return None