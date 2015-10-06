#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

from TwitterAPI import TwitterAPI

CONSUMER_KEY = "blzC40MytkH9HguJYBUcttxxg"
CONSUMER_SECRET = "Mw37mXO7sXUNazbUkUlfsfjSzQCMIXNZXD3wuSmJeQj1tvnm2e"
ACCESS_TOKEN_KEY = "2658435840-MjNaSPPQso4aMFK1C1SgB5S8ISlRSAlQsPLFB74"
ACCESS_TOKEN_SECRET = "iTF4QJcKlu4ZCOJbtbJTTGvO1xHjRSB5JZJCrdTjyJQrB"

api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)
count = 30
tweets =[[0 for x in range(count + 1)] for x in range(5)]
tweets[0][0] = "HackGT"
tweets[1][0] = "HackMIT"
tweets[2][0] = "HTN"
tweets[3][0] = "HackNY"
tweets[4][0] = "HackTX"


lang = "en"
since = ["2015-09-25", "2015-09-18", "2015-09-17", "2015-09-25", "2015-09-25"]
until = ["2015-09-27", "2015-09-21", "2015-09-21", "2015-09-28", "2015-09-28"]

for i in xrange(5):
	j = 1
	r = api.request('search/tweets', {'lang': lang, 'q': tweets[i][0], 'count': count, 'since':since[i], 'until':until[i]})
	for item in r:
		tweets[i][j] = item['text']
		j += 1

alchemyapi = AlchemyAPI()

sentiments = [[0 for x in range(2)] for x in range(5)]
counter 			= 	[0, 0, 0, 0, 0]

for i in xrange(5):
	for j in xrange(1, count + 1):
		response = alchemyapi.sentiment('text', tweets[i][j], {'showSourceText':1})
		
		print(json.dumps(response, indent=4))
		response['outputMode'] = 'json'

		if response['status'] == 'OK':
			if 'score' in response['docSentiment']:
				if(float(response['docSentiment']['score']) < 0):
					sentiments[i][1] += 1
				else:
					sentiments[i][0] += 1
				counter[i] +=1
		else:
			print (response['statusInfo'])

print("\n")
print("Positive Sentiment: ")

for i in xrange(5):
	answer = int((sentiments[i][0] * 100) / counter[i])
	print(tweets[i][0] + ": " + str(answer) + "%")













