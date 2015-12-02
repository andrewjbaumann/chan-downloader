import bs4
from bs4 import BeautifulSoup 
import json
import urllib
import urllib2
from urllib2 import urlopen

url = raw_input("What is the 4chan URL?")
lpath = raw_input("What is the path?")
images = list()

if "https://boards.4chan.org/" not in url:
	print "Error: not a legitimate 4chan URL"
else:
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
	html = urlopen(req)
	soup = BeautifulSoup(html, "lxml")
	for a in soup.findAll('a', href=True,attrs={'class':'fileThumb'}):
		images.append(a['href'][2:])
	for img in images:
		img = "https://" + img.replace('\\','/')
		imgName = img.split('/')[-1]
		print img
		urllib.urlretrieve(img, lpath+imgName)
		