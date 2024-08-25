from bs4 import BeautifulSoup
import requests
# Parse XML API using beautifulsoup
url = ("https://www.digikala.com/sitemap.xml")
xml = requests.get(url)

soup = BeautifulSoup(xml.content, 'lxml-xml')

# print(soup)

# get all location links
all_locs = soup.find_all("loc")
for loc in all_locs:
    print(loc.get_text())
