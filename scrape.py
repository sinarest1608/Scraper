import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

#For page 1
url = "https://www.tripadvisor.in/Attractions-g297583-Activities-Andaman_and_Nicobar_Islands.html"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html5lib')

category = []
for c in soup.find_all('div', attrs={'class':'ui_container attractions-attraction-overview-main-TopPOIs__container--3eHZU'}):
    for ca in c.find_all('span', attrs={'class':'attractions-category-tag-CategoryTag__category_tag--3_ylb'}):
        category.append(ca.text)

#print(len(category))
#print(category)

name = []
for t in soup.find_all('a', attrs={'class':'attractions-attraction-overview-pois-PoiInfo__name--SJ0a4'}):
    name.append(t.text)
#print(len(titles))
#print(titles)

review = []
for r in soup.find_all('div', attrs={'class':'ui_container attractions-attraction-overview-main-TopPOIs__container--3eHZU'}):
    for re in r.find_all('span', attrs={'class':'reviewCount styleguide-bubble-rating-BubbleRatingWithReviewCount__reviewCount--37tMc'}):
        review.append(re.text)
review = [flash.replace('review', '') for flash in review]
review = [g.replace('s', '') for g in review]
#print(len(review))
#print(review)


links = []
for l in soup.find_all('a', attrs={'class':'attractions-attraction-overview-pois-PoiInfo__name--SJ0a4'}):
    links.append("https://www.tripadvisor.in"+l.get('href'))
#print(len(links))



ratings = []
for k in links:
    URL = k
    beta = requests.get(URL)
    new_soup = BeautifulSoup(beta.text, 'html5lib')
    for m in new_soup.find_all('span', attrs={'class':'overallRating'}):
        ratings.append(m.text)
#print(len(ratings))
#print(ratings)

andaman_1 = pd.DataFrame( {'City':'Andaman & Nicobar Islands', 'Category': category, 'Name': name, 'Reviews':review, 'Rating':ratings} )
#andaman_1
#For page 2

data_2 = requests.get('https://www.tripadvisor.in/Attractions-g297583-Activities-oa30-Andaman_and_Nicobar_Islands.html')
soup_2 = BeautifulSoup(data_2.text, 'html5lib')

categories = []
for cat in soup_2.find_all('div', attrs={'class':'p13n_reasoning_v2'}):
    categories.append(cat.text)
categories = [w.replace('\n', '') for w in categories]
print(len(categories))
#print(categories)

names = []
links_2 = []
for na in soup_2.find_all('div', attrs={'class':'tracking_attraction_title listing_title'}):
    for i in na.find_all('a'):
        names.append(i.text)
        links_2.append('https://www.tripadvisor.in'+i.get('href'))
print(len(names))
#print(names)
print(len(links_2))
#print(links_2)

reviews = []
for re in soup_2.find_all('span', attrs={'class':'more'}):
    reviews.append(re.text)
reviews = [rev.replace('\n', '') for rev in reviews]
reviews = [revi.replace('reviews', '') for revi in reviews]
reviews = [revive.replace('review', '') for revive in reviews]
print(len(reviews))
#print(reviews)

ratings_2 = []
for ink in links_2:
    URL_2 = ink
    beta_2 = requests.get(URL_2)
    new_soup_2 = BeautifulSoup(beta_2.text, 'html5lib')
    for dp in new_soup_2.find_all('span', attrs={'class':'overallRating'}):
        ratings_2.append(dp.text)
print(len(ratings_2))
#print(ratings_2)

andaman_2 = pd.DataFrame( {'City':'Andaman & Nicobar Islands', 'Category':categories, 'Name':names, 'Reviews':reviews, 'Rating':ratings_2} )
#andaman_2 just to print

#For Page 3

data_3 = requests.get('https://www.tripadvisor.in/Attractions-g297583-Activities-oa60-Andaman_and_Nicobar_Islands.html#FILTERED_LIST')
soup_3 = BeautifulSoup(data_2.text, 'html5lib')

categories_3 = []
for cat in soup_2.find_all('div', attrs={'class':'p13n_reasoning_v2'}):
    categories_3.append(cat.text)
categories_3 = [w.replace('\n', '') for w in categories_3]
print(len(categories_3))
#print(categories)

names_3 = []
links_3 = []
for na in soup_2.find_all('div', attrs={'class':'tracking_attraction_title listing_title'}):
    for i in na.find_all('a'):
        names_3.append(i.text)
        links_3.append('https://www.tripadvisor.in'+i.get('href'))
print(len(names_3))
#print(names_3)
print(len(links_3))
#print(links_3)

reviews_3 = []
for re in soup_2.find_all('span', attrs={'class':'more'}):
    reviews_3.append(re.text)
reviews_3 = [rev.replace('\n', '') for rev in reviews_3]
reviews_3 = [revi.replace('reviews', '') for revi in reviews_3]
reviews_3 = [revive.replace('review', '') for revive in reviews_3]
print(len(reviews_3))
#print(reviews_3)

ratings_3 = []
for ink in links_2:
    URL_2 = ink
    beta_2 = requests.get(URL_2)
    new_soup_2 = BeautifulSoup(beta_2.text, 'html5lib')
    for dp in new_soup_2.find_all('span', attrs={'class':'overallRating'}):
        ratings_3.append(dp.text)
print(len(ratings_3))
#print(ratings_3)

andaman_3 = pd.DataFrame( {'City':'Andaman & Nicobar Islands', 'Category':categories_3, 'Name':names_3, 'Reviews':reviews_3, 'Rating':ratings_3} )
#andaman_3

#For Combining all the dataframes.
Andaman_total = pd.concat( [andaman_1, andaman_2, andaman_3], ignore_index=True)
#Andaman_total just to print

#To convert the dataframe to csv.
Andaman_total.to_csv('Andaman.csv')



