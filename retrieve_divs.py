import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def getDiv(url):
    if url.startswith("https://") or url.startswith("http://"):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup('div')
        for div in divs:
            print(div)
    else:
        url = 'https://' + url
        getDiv(url)

url = input('Enter: ')
getDiv(url)
            
