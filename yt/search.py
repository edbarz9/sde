from urllib.request import urlopen as uOpn
from bs4 import BeautifulSoup as bsoup

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup
