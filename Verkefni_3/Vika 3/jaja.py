import requests

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=vörðuskóli')

resp_json_payload = response.json()

print(resp_json_payload['results'][0]['geometry']['location'])