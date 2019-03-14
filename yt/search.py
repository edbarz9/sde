#!/usr/bin/python3
import os
import sys
from urllib.request import urlopen as uOpn
from urllib.request import urlretrieve as uRtv
from bs4 import BeautifulSoup as bsoup

def parseQuery():
    query = ""
    for i in range(len(sys.argv) - 2):
        query = query + sys.argv[i+1] + "+"

    query = query + sys.argv[i+2]
    return query

query = parseQuery()

ytSearchBase = "https://www.youtube.com/results?search_query="

url = ytSearchBase + query

thumbPath = "/tmp/ytSearchThumb/" + query + "/"
if not os.path.isdir(thumbPath):
    os.makedirs(thumbPath)

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
    #print(link)
    thumb = i.find('img').get('data-thumb')
    #print(thumb)
    try:
        uRtv(str(thumb), thumbPath + link + ".jpg")
    except:
        print("Could not save thumb")
        pass

os.system("cd "+ thumbPath +"&& sxiv -tr *")
