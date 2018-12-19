from bs4 import BeautifulSoup
import requests
 
def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            #print(link.string.strip())
            print(domain + href)
 
getPlaylistLinks("https://www.youtube.com/playlist?list=PLF38FCD363F7184B0")
