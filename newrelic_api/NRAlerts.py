##########################################################################################
##	FileName: 	NRAlerts.py 															##
##	Purpose:	Contains all New Relic API methods for 									##	
##				CRUD operations on APM and Infra alerts 								##
##	Author: 	Krishna Mudragada 														##
##########################################################################################

## Defs:: Imports 

import yaml
from requests_api import requestsApi
from configparser import ConfigParser, NoSectionError
from datetime import datetime as dt

## Defs:: File Scope Functions

def log(msg):
	print ('[%s]: %s' % (dt.now().isoformat(), msg))

def readConfig():
	config = yaml.load(open("config.yml"))
	return config

## Defs:: File Scope Objects

config = readConfig()
requestObj = requestsApi()
REQUEST_HEADER = dict()

## Defs:: Class Definition(s)


class NRAlerts:


	# For each account,
	#	1. GET All Alert Policies
	#	2. log all the alerts under the policies by type

	def get_all_alerts(self):

		newrelic_accounts = config['newrelic_accounts'].items()
		alert_types = config['alerts']['types'].items()

		for account, account_attributes in newrelic_accounts:
			if (account_attributes['status'].lower() == 'active'):
				alertPolicyList = self.get_alert_policies(account, account_attributes)
			

				for i in range(len(alertPolicyList)):
					## For Each Alert Policy
					alert_policy = alertPolicyList[i]
					policy_id = alert_policy['id']
					policy_name = alert_policy['name']

					## For Each Type of alert set
					for alert_type, alert_type_attributes in alert_types:
						response = self.get_alerts(policy_id, policy_name, alert_type, account_attributes, alert_type_attributes)
						alert_conditions = dict()

						if('conditions' in response):
							## for APM Alerts
							alert_conditions =  response['conditions']
						elif('data' in response):
							## for Infra Alerts
							alert_conditions= response['data']

						## Log all the alerts from the policy	
						self.log_alerts_from_policy(policy_name, alert_conditions)
			else:
				log("Account Not active: " + str(account))


	# For a given alert policy and list of alert conditions,
	#	1. log all the alerts under the policies

	def log_alerts_from_policy(self, policy_name, alert_conditions):
		if(alert_conditions != None):
			num_conditions = len(alert_conditions)
		else:
		## Not all conditions in each alert policy will have both APM and INFRA alerts
			num_conditions = 0
		
		## Choose only the conditions objects that have at least one alert
		if(num_conditions > 0):
			print('-' * len(policy_name))
			print(policy_name)
			print('-' * len(policy_name))

			for j in range(num_conditions):
				alertCondition = alert_conditions[j]
				if(alertCondition != None):
					print('\n')
					print(alertCondition['name'])
					print(alertCondition)
			print('\n')

	# For a given Type of Alerts,
	#	1. GET All Alert Conditions in a Policy
	#	2. log all the alerts under the policies

	def get_alerts(self, policy_id, policy_name, alert_type, account_attributes, alert_type_attributes):
		PAYLOAD =  dict()
		if (alert_type.lower() == 'apm'):
			PAYLOAD['policy_id'] = str(policy_id)
			REQUEST_HEADER['X-Api-Key'] = account_attributes['api_key']
			REQUEST_URL = alert_type_attributes['url']
		elif(alert_type.lower() == 'infra'):
			REQUEST_URL = alert_type_attributes['url'].replace('{REPLACE_POLICY_ID}', str(policy_id))
			REQUEST_HEADER['X-Api-Key'] = account_attributes['admin_api_key']

		alertsResponse = requestObj.request_json('GET', REQUEST_URL, REQUEST_HEADER, PAYLOAD)
		return alertsResponse

	# For a given Account,
	#	1. GET All Alert Policies in a Policy

	def get_alert_policies(self, account, account_attributes):
		log("Retrieving all alert policies for account.." + str(account))
		REQUEST_HEADER['X-Api-Key'] = account_attributes['api_key']
		REQUEST_URL = config['alerts']['policies']['url']
		response = requestObj.request_json('GET', REQUEST_URL, REQUEST_HEADER, None)
		log("Number of policies: "  + str(len(response['policies'])))
		return response['policies']

	def create_alert_policy(self, incident_preference, name):
		log("Creating new alert policy")
		alert_policy_data = self.prepare_alert_policy_string(incident_preference, name)

		response = requestObj.request_json('POST', URL_ALERT_POLICY, HEADER_GET_ALERTS, alert_policy_data)
		return response

	def prepare_alert_policy_string(self, incident_preference, name):
		policy = dict()
		policy['incident_preference'] = incident_preference
		policy['name'] = name
		return policy


	def update_alert_policy(self):
		log ("Updating an existing alert policy")



## Defs:: Main Function (optional)
