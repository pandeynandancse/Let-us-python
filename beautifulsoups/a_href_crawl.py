import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

htmls = urllib.request.urlopen('https://pandeynandancse.github.io/').read()
soup = BeautifulSoup(htmls,'html.parser')
tags = soup('a')
for tag in tags:
	print(tag.get('href',None))
