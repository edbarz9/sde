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
for i in sublist:
    print(i + " " + sublist[i])

months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

def date2int(date):
    date = date.replace("Published on ","")
    month = months[date[0:3]]
    year = date[10:12]
    day = date[4:6]
    dateIndex = 999999 - int(year + month + day)
    return str(dateIndex)

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup

def parseVids(channelId):
    ytchanbase = "https://www.youtube.com/channel/"
    url = ytchanbase + channelId + "videos"
    soup = soupMaker(url)
    tlist = soup.find_all('div',{'class':'yt-lockup-dismissable'})

    for l in tlist:
        link = l.find('a').get('href').replace('/watch?v=','')
        thumb = l.find('img').get('src')
        titletag = l.find('h3',{'class':'yt-lockup-title'})
        title = titletag.find('a').text.strip()
        duration = l.find('span',{'class':'video-time'}).text.strip()
        vidName = link + " " + title + " " + duration
        print(vidName)
