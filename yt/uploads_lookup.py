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
jsonPath = os.path.expanduser(subListPath)
subListJson = open(jsonPath).read()
data = json.loads(subListJson)
sublist = data['subs']
lastCheck = data['last']
newLast = lastCheck
ytwatch = "https://www.youtube.com/watch?v="

def dateIndxMkr(date):
    global newLast
    dateIndex = 999999 - int(date[2:4]+date[5:7]+date[8:10])
    if dateIndex < newLast:
        newLast = dateIndex
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
        try :
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
            if date >= lastCheck:
                break
            print(vidName)
        except:
            pass

def parseSub(channels):
    for c in channels:
        parseVids(channels[c])

def updateJson():
    global data
    data['last'] = newLast
    with open(jsonPath, 'w') as newJSON:
        json.dump(data, newJSON, sort_keys=True, indent=2)

parseSub(sublist)
updateJson()
print(lastCheck)
print(newLast)
