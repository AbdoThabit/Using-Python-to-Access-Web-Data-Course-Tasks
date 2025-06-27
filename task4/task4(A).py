import urllib.request
from bs4 import BeautifulSoup


url = 'http://py4e-data.dr-chuck.net/comments_1977159.html'

response = urllib.request.urlopen(url)
html_content = response.read()

soup = BeautifulSoup(html_content, 'html.parser')


spans = soup.find_all('span')
total_sum =0

for span in spans:
    # Extract text from the span
    text = span.text.strip()
    # Convert text to integer and add it to the total sum
    total_sum += int(text)

# Print the total sum
print(total_sum)