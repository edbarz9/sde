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
searchResults = searchResultSoup.find('ol',{'class':'item-section'})
searchResultList = searchResults.find_all('div', {'class':'yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix'})

for i in searchResultList:
    link = i.find('a').get('href').replace('/watch?v=','')
    print(link)
    thumb = i.find('img').get('data-thumb')
    print(thumb)
