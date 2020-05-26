from bs4 import BeautifulSoup
import requests

url = 'https://timesofindia.indiatimes.com/'

r = requests.get(url)

content = r.content

soup = BeautifulSoup(content, 'html5lib')

title = []

# for h2_tag in soup.find_all("h2"):
# 	a_tag = h2_tag.find('a')
# 	urls.append(a_tag.attrs['href'])

# for li in soup.find_all('li'):
# 	a_tag = li.find('a')
# 	title.append(a_tag.attrs['title'])

# tag = soup.find_all("a")
# print(tag.attrs['title'])

mydivs = soup.find_all('div')
for div in mydivs: 
    if (div["class"] == "top-story"):
        print(div)