import oauth2
import json
import urllib.parse

consumer_key = 'iwEFYgWx7ZpAf4z1fmu8bnNzt'
consumer_secret = 'SBuzrYeY6C6iMB7ZU69l4XqcSkrJ1Yw9PeOw8HaIfpbPNtPBsJ'

access_token = '82901621-7HmtSKstGFFtvO4D4ITVVGRG2cnRDf7NdQKnEARUx'
token_secret = 'V1rchNW41z7XmzVjU1Sn6KAUehWsW1RFE6F2EKeD3rPNR'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(access_token, token_secret)

cliente = oauth2.Client(consumer, token)

search = input('Digite o que deseja pesquisar: ')
query_cod = urllib.parse.quote(search, safe='')
req = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_cod)
dec = req[1].decode()
requestObject = json.loads(dec)
print(type(requestObject))
twittes = requestObject['statuses']
print(twittes)

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()




