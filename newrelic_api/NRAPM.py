## NR APM

## Global Variables

REQUEST_HEADER = dict()

## CLASS
class NRAPM:

	def get_all_applications(self):
		for account, account_attributes in config['newrelic_accounts'].items():
				
				## For Each New Relic Account
			for alert_type, alert_type_attributes in config['alerts']['conditions'].items():
				
				## For Each type of Alerts (APM/Browser/Mobile, INFRA)

				## GET alert Policies for each account using the account's attributes
				alertPolicyList = self.get_alert_policies(account, account_attributes)
				for i in range(len(alertPolicyList)):

					## For Each Alert Policy
					alert_policy = alertPolicyList[i]
					policy_id = alert_policy['id']
					policy_name = alert_policy['name']

					response = self.get_alerts(policy_id, policy_name, alert_type, account_attributes, alert_type_attributes)
					alertConditions = dict()
					if('conditions' in response):
						## Format for APM Alerts
						alertConditions =  response['conditions']
					elif('data' in response):
						## Format for Infra Alerts
						alertConditions= response['data']

					## Log all the alerts from the policy	
					self.log_alerts_from_policy(policy_name, alertConditions)



	def log_alerts_from_policy(self, policy_name, alertConditions):
		if(alertConditions != None):
			numConditions = len(alertConditions)
		else:
		## Not all conditions in each alert policy will have both APM and INFRA alerts
			numConditions = 0
		
		## Choose only the conditions objects that have at least one alert
		if(numConditions > 0):
			print('-' * len(policy_name))
			print(policy_name)
			print('-' * len(policy_name))

			for j in range(numConditions):
				alertCondition = alertConditions[j]
				if(alertCondition != None):
					print('\n')
					print(alertCondition['name'])
			print('\n')

	def get_alerts(self, policy_id, policy_name, alert_type, account_attributes, alert_type_attributes):
		PAYLOAD =  dict()
		if (alert_type.lower() == 'apm'):
			PAYLOAD['policy_id'] = str(policy_id)
			REQUEST_HEADER['X-Api-Key'] = account_attributes['api_key']
			REQUEST_URL = alert_type_attributes['url']
		elif(alert_type.lower() == 'infra'):
			url_get_alerts = URL_GET_INFRA_ALERTS.replace('REPLACE_POLICY_ID', str(policy_id))
			REQUEST_HEADER['X-Api-Key'] = ADMIN_API_KEY

		alertsResponse = requestObj.request_json('GET', REQUEST_URL, REQUEST_HEADER, PAYLOAD)
		return alertsResponse


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

