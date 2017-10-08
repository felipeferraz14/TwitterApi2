import tweepy
from textblob import TextBlob as tb
import numpy as np

consumer_key = 'iwEFYgWx7ZpAf4z1fmu8bnNzt'
consumer_secret = 'SBuzrYeY6C6iMB7ZU69l4XqcSkrJ1Yw9PeOw8HaIfpbPNtPBsJ'

access_token = '82901621-7HmtSKstGFFtvO4D4ITVVGRG2cnRDf7NdQKnEARUx'
token_secret = 'V1rchNW41z7XmzVjU1Sn6KAUehWsW1RFE6F2EKeD3rPNR'

consumer = tweepy.OAuthHandler(consumer_key, consumer_secret)
consumer.set_access_token(access_token, token_secret)

api = tweepy.API(consumer)
public_tweets = api.search()

analysis = None

for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    print(analysis.sentiment.polarity)


print('A Média de sentimento' + str(np.mean(analysis.sentiment.polarity)))
