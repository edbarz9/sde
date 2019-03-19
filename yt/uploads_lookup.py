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
#print(type(sublist))
for i in sublist:
    print(i + " " + sublist[i])

months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

def date2int(date):
    date = date.replace("Published on ","")
    month = months[date[0:3]]
    return month

dateTest = "Published on Dec 15, 2018"
print(date2int(dateTest))

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup

url = "https://www.youtube.com/channel/UC0NCbj8CxzeCGIF6sODJ-7A/videos"

tsoup = soupMaker(url)
#tsoup = soupMaker("https://www.youtube.com/user/thinkerview/videos")

tlist = tsoup.find_all('div',{'class':'yt-lockup-dismissable'})

for l in tlist:
    link = l.find('a').get('href').replace('/watch?v=','')
    thumb = l.find('img').get('src')
    titletag = l.find('h3',{'class':'yt-lockup-title'})
    title = titletag.find('a').text.strip()
    duration = l.find('span',{'class':'video-time'}).text.strip()
    vidName = link + " " + title + " " + duration
    print(vidName)
