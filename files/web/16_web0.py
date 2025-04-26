#spider
def extractHrefs(soup):
    hrefs=[]
    for i in range (0,len(soup)):
        hrefs.append(soup[i]['href'])
    return hrefs
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urls= {'http://web-16.challs.olicyber.it'}
while urls:
    url=urls.pop()
    print("tocca a :"+url)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for h1 in soup.find_all('h1'):
        if 'flag' in h1.text:
            while(True):
                print(h1)
    aTags=extractHrefs(soup.find_all('a'))
    print(aTags)
    for a in aTags:
        urls.add(urljoin(url,a))
    




