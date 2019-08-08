##########################################################################################
##	FileName: 	main.py 																##
##	Purpose:	Main Caller to retrieve, update and create new alerts as necessary		##	
##	Author: 	Krishna Mudragada 														##
##########################################################################################


## Defs:: Imports 

import yaml
from requests_api import requestsApi
from configparser import ConfigParser, NoSectionError
from datetime import datetime as dt
from NRAlerts import NRAlerts


## Defs:: File Scope Functions


## Defs:: File Scope Objects


## Defs:: Class Definition(s)


## Defs:: Main Function

def main():
	nrAlertsObj = NRAlerts()
	nrAlertsObj.get_all_alerts()

if __name__ == "__main__":
        main()