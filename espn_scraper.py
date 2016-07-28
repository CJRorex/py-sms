from bs4 import BeautifulSoup
import urllib2
import re

def espn_headline_scraper():
	'''
	Returns list of top headlines currently on espn.com 
	'''
	headlines_list = []
	links = []
	r = urllib2.urlopen('http://www.espn.com/').read()
	soup = BeautifulSoup(r)
	headline_tags = soup.find_all("div", {"class": "headlines"})
	for div in headline_tags:
		for ul in div.find_all("ul"):
			for li in ul.find_all("li"):
				headlines_list.append (li.get_text())
				for a in li.find_all("a"):
					links.append ('espn.go.com' + a['href'])

	return headlines_list , links


print espn_headline_scraper()

def nyt_headline_count(needle):
	'''
	Given a needle (must be lowercase!)
	Returns number of times needle appears in 
	headline on nytimes.com
	'''

	needle = needle.lower()
	needle_count = 0

	r = urllib2.urlopen('http://www.nytimes.com/').read()
	soup = BeautifulSoup(r)

	news_item_tags = soup.find_all("h2", {"class": "story-heading"})
	news_item_tags += soup.find_all("h3", {"class": "story-heading"})

	news_items = []

	for elem in news_item_tags:
		news_items.append(elem.get_text())

	# print news_items

	for item in news_items:
		if needle in item.lower():  # making it lower case is key!
			needle_count += 1

	# print "How many %s's in the news today? %d" % (needle, needle_count)

	return needle_count

def all_text_count(needle, url):
	'''
	returns count of needle in visible text of url
	'''
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	texts = soup.findAll(text=True)

	def visible(element):
	    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
	        return False
	    elif re.match('<!--.*-->', unicode(element)):
	        return False
	    return True

	visible_texts = filter(visible, texts)
	visible_texts = visible_texts

	needle = needle.lower()
	needle_count = 0

	for elem in visible_texts:
		elem = elem.lower()
		if needle in elem:
			needle_count += elem.count(needle)

	return needle_count
