import requests
import json
import pprint

url = 'https://widget.songle.jp/api/v1/song/chorus.json'
headers = {"Content-Type": "application/json"}
data = {'url':'https://www.youtube.com/watch?v=PqJNc9KVIZE'}
json_data = json.dumps(data)
sabi = requests.get(url, headers=headers,data=json_data)
print(sabi)
data = json.loads(sabi.text)
pprint.pprint(data['chorusSegments'][0]['repeats'][0]['start'])
