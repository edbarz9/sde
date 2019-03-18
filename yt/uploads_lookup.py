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
subFile = open(subListPath,'r')
subListJson = json.loads(subFile)
subFile.close()
print(subListJson['test'])

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
