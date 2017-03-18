# Uses twitter package as an API accessor for tweets
import time
import twitter
import tokens
from speech1 import speechify as say

api = twitter.Api(
consumer_key=tokens.consumer_key,
consumer_secret=tokens.consumer_secret,
access_token_key=tokens.access_token_key,
access_token_secret=tokens.access_token_secret)

#print(api.VerifyCredentials())
last_id = 0L 
while(1):
	time.sleep(10)
	msgs = api.GetDirectMessages(count=5)
	latest = msgs[0].AsDict()
	second_latest = msgs[1].AsDict()	
	if latest[u'id'] == last_id:
		"do nothing"
		continue
	elif second_latest[u'id'] == last_id:
		# Process latest message
		last_id = latest[u'id']
		say("Message from {} says: {}".format(latest[u'sender'][u'name'], latest[u'text']))
	else :
		# Process 2 new messages
		last_id = latest[u'id']
		say("Message from {} says: {}".format(second_latest[u'sender'][u'name'], second_latest[u'text']))
		say("Message from {} says: {}".format(latest[u'sender'][u'name'], latest[u'text']))
		
