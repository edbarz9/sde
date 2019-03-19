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
sublist = json.loads(subListJson)
#for i in sublist:
#    print(i + " " + sublist[i])

months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

def dateIndxMkr(date):
    dateIndex = 999999 - int(date[2:4]+date[5:7]+date[8:10])
    return str(dateIndex)

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
    tlist = soup.find_all('div',{'class':'yt-lockup-dismissable'})

    for l in tlist:
        link = l.find('a').get('href').replace('/watch?v=','')
        thumb = l.find('img').get('src')
        titletag = l.find('h3',{'class':'yt-lockup-title'})
        title = titletag.find('a').text.strip()
        duration = l.find('span',{'class':'video-time'}).text.strip()
        vidsoup = soupMaker("https://www.youtube.com/watch?v=" + link)
        datestr = vidsoup.find('meta',{'itemprop':'datePublished'}).get("content")
        date = dateIndxMkr(datestr)
        vidName = date + " " + link + " " + title + " " + duration
        print(vidName)

def parseSub(channels):
    for c in channels:
        parseVids(channels[c])

parseSub(sublist)
