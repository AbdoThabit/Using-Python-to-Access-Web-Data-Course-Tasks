import urllib.request ,urllib.parse
import json

url = 'https://py4e-data.dr-chuck.net/opengeo?'
parms = dict()
parms['q'] = 'Universidad de San Carlos de Guatemala'
url+= urllib.parse.urlencode(parms)
   
    
response = urllib.request.urlopen(url)


jsonContent = response.read()
data = json.loads(jsonContent)
 
plus_code = data['features'][0]['properties']['plus_code']

print("Plus Code:", plus_code) 
    
