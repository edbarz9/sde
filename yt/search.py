#!/usr/bin/python3
import os
import sys
import subprocess
from urllib.request import urlopen as uOpn
from urllib.request import urlretrieve as uRtv
from bs4 import BeautifulSoup as bsoup

def parseQuery(q):
    query = ""
    for i in q.split():
        query = query + i + "+"

    query = query[:-1]
    return query

dq = subprocess.check_output('echo "search youtube" | dmenu', shell=True)
dq = str(dq).replace("b'","").replace("\\n'","")

query = parseQuery(dq)
print(query)

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

try:
    os.system('notify-send "searching for:' + dq + '"')
except:
    pass

searchResultSoup = soupMaker(url)
searchResults = searchResultSoup.find('ol',{'class':'item-section'})
searchResultList = searchResults.find_all('div', {'class':'yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix'})

for i in searchResultList:
    try:
        atag = i.find('a')
        titletag = i.find('h3',{'class':'yt-lockup-title'})
        title = titletag.find('a').get('title')
        link = atag.get('href').replace('/watch?v=','')
        duration = i.find('span',{'class':'video-time'}).text.strip()
        print(title)
        print(link)
        print(duration)
        thumb = i.find('img').get('data-thumb')
        #print(thumb)
        uRtv(str(thumb), thumbPath + link + " " + title + " " + duration + ".jpg")
    except:
        print("Could not save thumb")
        pass

os.system("cd "+ thumbPath +"&& sxiv -tr *")
