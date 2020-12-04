from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

site = 'https://news.google.com/news/rss'
op = urlopen(site) #Open that site
rd = op.read() #read data from site
op.close()   # close the object
sp_page = soup(rd,features="xml") #scrapping data from site
news_list = sp_page.find_all('item') #finding news

# can alter if necessary
# example: put print(news_list) to check all the news in the page!

newslist = []

for news in news_list:
    newsarticle = {
        'title' : news.title.text,
        'link' : news.link.text,
        'date' : news.pubDate.text
    }
    newslist.append(newsarticle)

# feel free to edit here onwards
print(newslist)
print(newslist[1])
print(newslist[1]['title'])
print(newslist[1]['link'])
print(newslist[1]['date'])

