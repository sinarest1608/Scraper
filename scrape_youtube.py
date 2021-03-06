import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

#For scraping
def scrape(url):
    
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html5lib") #creating soup object
    title = [] #extracting title clips.
    for i in soup.find_all('tr'):
        title.append(i.get('data-title'))
    links = []
    res=soup.find_all('a',{'class':'pl-video-title-link'})
    for l in res:
        links.append("https://www.youtube.com"+l.get("href"))

    #For extracting likes and dislikes on a particular video

    likes = []
    dislikes = []
    views = []
    for linked in links:
        URL = linked
        new_data = requests.get(URL)
        new_soup = BeautifulSoup(new_data.text, 'html5lib')

        for v in new_soup.find_all('div', attrs={'class':'watch-view-count'}):
            views.append(v.text.strip())
        for j in new_soup.find_all('button', attrs={'title':'I like this'}):
            likes.append(j.span.text)
        for d in new_soup.find_all('button', attrs={'title':'I dislike this'}):
            dislikes.append(d.span.text)
            break
    convert(title, links, views, likes, dislikes)
#To convert/ merge the lists into a dataframe using Pandas
def convert(title, links, views, likes, dislikes):
    df = pd.DataFrame( {"Video": title, "Link": links, "Views": views, "Likes": likes, "Dislikes": dislikes})

    #Convert the Dataframe to a csv.
    df.to_csv('Youtube_sinarest.csv')
  
url = "your url"
scrape(url)

   
