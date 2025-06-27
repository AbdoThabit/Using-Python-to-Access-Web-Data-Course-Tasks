import urllib.request
import json

url = 'https://py4e-data.dr-chuck.net/comments_1977162.json'

response = urllib.request.urlopen(url)


jsonContent = response.read()

 
sum =0
info = json.loads(jsonContent)


for comment in info['comments']:
    sum += int(comment['count'])

print(sum)    
    
