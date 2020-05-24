from bs4 import BeautifulSoup

import requests

url = "https://www.worldometers.info/coronavirus/country/india/"

r = requests.get(url)

content = r.content

soup = BeautifulSoup(content,"lxml")


for div in soup.find_all("div",{"id":"maincounter-wrap"}):
	title = div.find("h1").get_text()
	print(title)
	cases = div.find("span").get_text()
	print(cases)
