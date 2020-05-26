import requests
from bs4 import BeautifulSoup

r = requests.get("http://idrw.org/").content

soup = BeautifulSoup(r,"html5lib")

title = []
content = []
a = 0

for i in soup.find_all("h2", {"class": "art-postheader entry-title"}):
	title.append(i.getText())

for j in soup.find_all("div", {"class": "art-postcontent clearfix"}):
	content.append(j.getText())

content.pop(0)

for i in range(2):
	content.pop(-1)

for i in title:
	print(i)
	print(content[a])
	a=a+1
