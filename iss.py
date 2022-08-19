import requests
import json

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    response_dict = json.loads(response.text)
    position = response_dict['iss_position']
    print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])
else:
    print("Houston, we've got a problem: ", response.status_code)
