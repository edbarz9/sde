from urllib.request import urlopen as uOpn
from bs4 import BeautifulSoup as bsoup

query = "cocovoit"

ytSearchBase = "https://www.youtube.com/results?search_query="

url = ytSearchBase + query

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup

searchResultSoup = soupMaker(url)
print(searchResultSoup)
