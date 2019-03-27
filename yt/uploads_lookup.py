import os
import json
from urllib.request import urlopen as uOpn
from urllib.request import urlretrieve as uRtv
from bs4 import BeautifulSoup as bsoup
from configparser import ConfigParser

confpath = os.path.expanduser('~/.config/blbs.conf')

parser = ConfigParser()
parser.read(confpath)

subListPath = parser.get('youtube', 'subscriptions')
subListJson = open(os.path.expanduser(subListPath)).read()
data = json.loads(subListJson)
sublist = data['subs']
lastCheck = data['last']
ytwatch = "https://www.youtube.com/watch?v="

def dateIndxMkr(date):
    dateIndex = 999999 - int(date[2:4]+date[5:7]+date[8:10])
    return dateIndex

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup

def parseVids(channel):
    channelId = channel['id']
    channelType = channel['type']
    ytchanbase = "https://www.youtube.com/" + channelType + "/"
    url = ytchanbase + channelId + "/videos"
    print(url)
    soup = soupMaker(url)
    tlist = soup.find_all('div', \
        {'class':'yt-lockup-dismissable'})
    for l in tlist:
        link = l.find('a').get('href').replace('/watch?v=','')
        thumb = l.find('img').get('src')
        titletag = l.find('h3',{'class':'yt-lockup-title'})
        title = titletag.find('a').text.strip()
        duration = l.find('span', \
            {'class':'video-time'}).text.strip()
        vidsoup = soupMaker(ytwatch + link)
        datestr = vidsoup.find('meta', \
            {'itemprop':'datePublished'}).get("content")
        date = dateIndxMkr(datestr)
        vidName = str(date) + " " + link + " " + \
                  title + " " + duration
        print(vidName)
        if date >= lastCheck:
            break

def parseSub(channels):
    for c in channels:
        parseVids(channels[c])

parseSub(sublist)
