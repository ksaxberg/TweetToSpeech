# Uses twitter package as an API accessor for tweets
import time
import twitter
import tokens
from speech1 import speechify as say

def mentions(api, last_id=0L):
	if last_id != 0L:
		msgs = api.GetMentions(count=5, since_id=last_id)
	else:
		msgs = api.GetMentions(count=5)
	if len(msgs) == 0:
		return last_id
	for msg in [x.AsDict() for x in msgs[::-1]]:
		say("Mention from {} says: {}".format(msg[u'sender'][u'name'], msg[u'text']))
		
	latest = msgs[0].AsDict()
	last_id = latest[u'id']
	return last_id

def directMessages(api, last_id=0L):
	if last_id != 0L:
		msgs = api.GetDirectMessages(count=3, since_id=last_id)
	else:
		msgs = api.GetDirectMessages(count=3)
	if len(msgs) == 0:
		return last_id
	for msg in [x.AsDict() for x in msgs[::-1]]:
		say("Message from {} says: {}".format(msg[u'sender'][u'name'], msg[u'text']))
	latest = msgs[0].AsDict()
	last_id = latest[u'id']
	return last_id
			
if __name__== "__main__":
	api = twitter.Api(
	consumer_key=tokens.consumer_key,
	consumer_secret=tokens.consumer_secret,
	access_token_key=tokens.access_token_key,
	access_token_secret=tokens.access_token_secret)
	#print(api.VerifyCredentials())
	
	# Rate limit for DM: 1/min
	# Rate limit for Mentions: 4/min
	last_dm = 0L
	last_mention = 0L
	dm_count = 0
	while(True):
		time.sleep(16)
		last_mention = mentions(api, last_mention)
		if dm_count == 3:
			last_dm = directMessages(api, last_dm)
		dm_count = (dm_count + 1) % 4
