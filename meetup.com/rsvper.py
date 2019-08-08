import requests, json
import pandas as pd
from requests_api import requestsApi 
from configparser import ConfigParser, NoSectionError
from datetime import datetime as dt

API_BASE_URL = 'https://api.meetup.com/'
EVENTS_URL =  'https://api.meetup.com/2/events'
RSVPS_URL = 'https://api.meetup.com/2/rsvps'
POST_RSVP_URL = 'https://api.meetup.com/rsvp'
GROUPS_URL = 'https://api.meetup.com/2/groups'
CONFIG_FILENAME = 'meetup.cfg'
API_KEY = '4371d792278345c6a141947614b3950'
MEMBER_ID = '7093938' 

apiObj = requestsApi()

def log(msg):
	print ('[%s]: %s' % (dt.now().isoformat(), msg))

def get_config():
	config = ConfigParser()
	try:
		with open(CONFIG_FILENAME) as f:
			config.readfp(f)	
	except IOError:
		sys.exit('Cannot read from %s' % CONFIG_FILENAME)

	return config

class RSVPer:
	def rsvp_for_groups(self):
		log("Attempting to read config file - meetup.cfg..")
		config = get_config()
		log("Done Reading config file" )

		try:
			log("Looking up for groups from config...")
			groups = config.sections()
		except NoSectionError:
			sys.exit('It seems your %s file is corrupt. ' % CONFIG_FILENAME)

		for group in groups:
			log("Checking on %s for RSVPs.." %(group))
			for group_id in config[group]:
				log("[%s]-[%s] - Attempting to RSVP for any open group events.." % (group, config[group][group_id]))
				self.rsvp_for_group_events(config[group][group_id])

	def rsvp_for_group_events(self,group_id):
		# Loops through a group's (specified by group_id) upcoming events and 
		# RSVP's yes if an event doesn't have a current RSVP. '''

		events = self.get_events(group_id)
		if not events:
			log ("Didn't find any events in the meetup..Skipping..")
		else:
			for event in events:
				group_name = event['group']['name']
				event_name = event['name']
				event_id = event['id']
				event_url = event['event_url']
				my_rsvp = self.get_event_rsvp(event['id'])
				if my_rsvp:
					log ('[%s] RSVP\'d yes to "%s" (%s)' % (group_name, event_name,event_url))
					if event['yes_rsvp_count'] >= event['rsvp_limit']:
						log('[%s] Cannot RSVP to %s, the event is full. Please visit %s to add yourself to the waiting list if one is available.' % (event['group']['name'], event['name'], event['event_url']))
					elif rsvp_yes(event_id):
						log('[%s] RSVP\'d yes to "%s" (%s)' % (group_name, event_name,event_url))
					else:
						log('[%s] Problem RSVP\'ing to event %s: %s : %s' % (group_name,event_id,event_name,event_url))
				else:
					log('[%s] No new non-RSVP\'d events.' % group_name)

	def get_events(self, group_id):
		log("[%s]- GET /2/events " % group_id)
		resp = apiObj.GET_json(EVENTS_URL, {'group_id': group_id, 'key': API_KEY})
		print (resp)
		events = resp['results']
		return events

	def get_event_memberDF(self, rsvps):
		# Returns all the members data having member details, response (yes/no) and the RSVP'ed date
		df = pd.DataFrame(rsvps)
		memberData = df[['member', 'response', 'created']]
		memberData['created'] =  pd.to_datetime(memberData['created'], unit='ms')
		memberSeries = pd.Series(memberData['member'], index=['member_id', 'name'])
		print (memberSeries)
		return memberData

	def get_event_rsvp(self, event_id):
		log("[%s]- GET /2/rsvps" % event_id)
		# Returns the current member's RSVP for a given event_id. An empty list is
		# returned if the member hasn't RSVP'd yet.
		resp = apiObj.GET_json(RSVPS_URL, {'event_id': event_id, 'key': API_KEY})
		rsvps = resp['results']
		memberDF = self.get_event_memberDF(rsvps)
		# print(memberDF)


def main():
	rsvpObj = RSVPer()
	rsvpObj.rsvp_for_groups()

if __name__ == "__main__":
	main()
