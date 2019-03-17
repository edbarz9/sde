#!/usr/bin/python3
import os
import sys
import subprocess
from urllib.request import urlopen as uOpn
from urllib.request import urlretrieve as uRtv
from bs4 import BeautifulSoup as bsoup

cliMode = False

def parseArg():
    global cliMode
    query = ""
    if len(sys.argv) > 1:
        cliMode = True
        i = -1
        for i in range(len(sys.argv) - 2):
            query = query + sys.argv[i+1] + "+"

        query = query + sys.argv[i+2]
    return query

def parseQuery(q):
    query = ""
    for i in q.split():
        query = query + i + "+"

    query = query[:-1]
    return query

query = parseArg()

if not cliMode:
    dq = subprocess.check_output('echo "search youtube" | dmenu', shell=True)
    dq = str(dq).replace("b'","").replace("\\n'","")
    query = parseQuery(dq)

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

vidIdx = 0
vList = []
for i in searchResultList:
    try:
        atag = i.find('a')
        titletag = i.find('h3',{'class':'yt-lockup-title'})
        title = titletag.find('a').get('title')
        link = atag.get('href').replace('/watch?v=','')
        duration = i.find('span',{'class':'video-time'}).text.strip()
        #print(title)
        #print(link)
        #print(duration)
        if not cliMode:
            thumb = i.find('img').get('data-thumb')
            uRtv(str(thumb), thumbPath + link + " " + title + " " + duration + ".jpg")
        else:
            vList.append([vidIdx,link,title])
            print(str(vidIdx) + " " + title + " " + duration)
            vidIdx = vidIdx + 1
    except:
        print("Could not save thumb")
        pass

if not cliMode:
    os.system("cd "+ thumbPath +"&& sxiv -tr *")
else:
    dln = input("download vid n°? ")
    try:
        print('start downloading' + vList[int(dln)][2])
        vId = vList[int(dln)][1]
        ytBase = "https://www.youtube.com/watch?v="
        ytLink = ytBase + vId
        os.system('youtube-dl --write-thumbnail -f webm '+ ytLink +' -o /tmp/ytdowns/'+ vId +'".webm" && notify-send "download finished"')
    except:
        print("not a number")
