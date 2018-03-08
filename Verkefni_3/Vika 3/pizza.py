import json,requests,pprint
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='EQXBZCLVIEX4HUG3XQA1PHWJTI1243XQVTYIFTKJ5MNF3DW1',
  client_secret='K0CUFGTID3XP1ZN1NH3WKJ250HSG1ZP0X1LV0EQYFVKS4Y0R',
  v='20170801',
  ll='64.126521,-21.817439',
  query='pizza',
  limit=4000
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
for x in data:
  if data['items']
