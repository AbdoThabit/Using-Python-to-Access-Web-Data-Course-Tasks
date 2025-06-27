import urllib.request
from bs4 import BeautifulSoup

name = ""
url = 'http://py4e-data.dr-chuck.net/known_by_Serene.html'
count = 0
while count < 7:
    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all('a')
    url = tags[17].get('href')
    name =tags[17].text
    count+=1
    

    
print(name)