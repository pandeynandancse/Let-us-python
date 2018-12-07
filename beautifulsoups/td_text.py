import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

htmls = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(htmls,'html.parser')
tags = soup('td')
for tag in tags:
	print(tag.text)



# extracting table data content 
