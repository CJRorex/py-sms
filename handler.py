from bs4 import BeautifulSoup
import urllib2

def response_handler(body):
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
    message = ""
    for l in links:
        message = message + "\n" + l
    return message

    
