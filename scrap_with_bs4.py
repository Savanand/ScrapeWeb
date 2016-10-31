import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    links = soup.find_all("a")
    for link in links:
        #    if "http" in link.get("href"):
        print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
    g_data = soup.find_all("div", {"class" : "info"})
    #        print item.contents[1].find_all("div",{"class": "phones phone primary"})[0].text
    for item in g_data:
        print item.contents[0].find_all("a", {"class": "business-name"})[0].text
        try:
            print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
            print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',', '')
            print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
            print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(["li","div"], {"class": "primary"})[0].text
        except:
            pass


base_url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=San+Jose%2C+CA"
urlpage2 = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=San+Jose%2C+CA&page=2"
urlp = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=San+Jose%2C+CA"+ "&page=2"
pages = 5

fetch_data(base_url)
for page in range(2, pages):
    temp_url= base_url + "&page=" + str(page)
    fetch_data(temp_url)

