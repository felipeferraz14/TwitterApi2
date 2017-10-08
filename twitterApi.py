import oauth2
import json
from textblob import TextBlob as tb
import numpy as np
import tweepy

consumer_key = 'iwEFYgWx7ZpAf4z1fmu8bnNzt'
consumer_secret = 'SBuzrYeY6C6iMB7ZU69l4XqcSkrJ1Yw9PeOw8HaIfpbPNtPBsJ'

access_token = '82901621-7HmtSKstGFFtvO4D4ITVVGRG2cnRDf7NdQKnEARUx'
token_secret = 'V1rchNW41z7XmzVjU1Sn6KAUehWsW1RFE6F2EKeD3rPNR'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(access_token, token_secret)
client = oauth2.Client(consumer, token)

consumerNew = tweepy.OAuthHandler(consumer_key, consumer_secret)
consumerNew.set_access_token(access_token, token_secret)
api = tweepy.API(consumerNew)

req = client.request('https://api.twitter.com/1.1/trends/place.json?id=560743')

dec = req[1].decode()
requestObject = json.loads(dec)

analysis = None

for twit in requestObject:
    var = twit['trends']

    for trends in var:
        twt = trends['name']
        url = trends['url']
        vol = int
        try:
            vol = int((trends['tweet_volume']))
        except Exception:
            vol = 0
        list = []
        list.append(vol)
        list.append(twt)
        list.append(url)
        print("The Tweet: "+list[1])

        public_tweets = api.search(list[1])

        for tweet in public_tweets:
            analysis = tb(tweet.text)

        print('The Sentiment Average ' + str(np.mean(analysis.sentiment.polarity)))
        print()


