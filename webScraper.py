from urllib.request import *
from bs4 import BeautifulSoup
import os

baseurl = "http://www.dot.state.mn.us/traffic/data/reports-hrvol-atr.html"
website = "http://www.dot.state.mn.us"
soup = BeautifulSoup(urlopen(baseurl))
links=soup.find_all("a", href = True)
for link in links:
    #print(link['href'])
    if (link.text == "TXT"):
        temp = link['href'].split("Hourly_Volume")
        print(website+link['href'])
        last_two=str(temp[-1])
        first=last_two.split('/')
        directory = first[1]
        if not os.path.exists('./rawData/'+directory):
            os.makedirs('./rawData/'+directory)
        urlretrieve(website+link['href'], "./rawData"+str(temp[-1]))
