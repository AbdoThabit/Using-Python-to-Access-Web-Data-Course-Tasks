import urllib.request
import xml.etree.ElementTree as ET

url = 'https://py4e-data.dr-chuck.net/comments_1977161.xml'

response = urllib.request.urlopen(url)


xml_content = response.read()

 
sum =0
tree = ET.fromstring(xml_content)
counts = tree.findall('comments/comment/count')

for count in counts:
    sum += int(count.text)

print(sum)    
    
