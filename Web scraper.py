import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


def make_soup (url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdatasaved=""
soup = make_soup("https://www.basketball-reference.com/boxscores/")
for record in soup.findAll('tr'):
    playerdata =""
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
    playerdatasaved = playerdatasaved + "\n" + playerdata [1:]

#header="W, L, W/l%, GB, PS/G, PA/G,"+"\n"
#file = open(os.path.expanduser("basketball.csv"),"wb")
#file.write(bytes(header, encoding="ascii",errors='ignore'))
#file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))