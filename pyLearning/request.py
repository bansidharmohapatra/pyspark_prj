import requests
import json

response= requests.get("http://api.stackexchange.com/2.2/badges?order=desc&sort=rank&site=stackoverflow")

for data in response.json()['items']:
    print(data['name'])

#print(response.json()['items']['name'])