import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

htmls = urllib.request.urlopen('https://www.imdb.com/').read()
soup = BeautifulSoup(htmls,'html.parser')
tags = soup('link')
for tag in tags:
	x = tag.get('href',None)
	if x == "#":
		continue
	elif ".html" in x:
		continue
	else:
		print(x)
