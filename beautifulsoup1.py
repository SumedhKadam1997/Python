import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.whitehouse.gov/briefings-statements/')

content = r.content

soup = BeautifulSoup(content, 'html5lib')

urls = []

for h2_tag in soup.find_all("h2"):
	a_tag = h2_tag.find('a')
	urls.append(a_tag.attrs['href'])

print(urls)