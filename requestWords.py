import requests
import json

req = requests.get('https://www.trendsmap.com/#')

#dec = request.decode()
#requestObject = json.loads(dec)
print(req.text)