
def NRAlerts:
	def get_alerts(self):
		get_alert_policies()
	def get_alert_policies(self):
		alert_policy_url = 'https://api.newrelic.com/v2/alerts_policies.json'


def main():
        nrAlertsObj = NRAlerts()
        nrAlertsObj.get_alerts()

if __name__ == "__main__":
        main()