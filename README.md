# news-scrapper
News crapping with Python BeautifulSoup from rss web feed

Change the source at line 4
Sources to be considered:
Google News: https://news.google.com/news/rss
Yahoo Finanace: https://finance.yahoo.com/news/rssindex

For all other RSS Web feed such as BBC, Reddit, CNBC, CNN, NYT or more, visit:
https://blog.feedspot.com/world_news_rss_feeds/

From Line 10 onwards is optional
Replace Line 10 with just print(news_list) is you desire just to see the whole list

Note: The output will be in terms of dictionary in a list.
Example: [ .... {'title': 'The latest on the coronavirus pandemic and vaccines: Live updates - CNN', 'link': 'https://news.google.com/__i/rss/rd/articles/CBMiaWh0dHBzOi8vd3d3LmNubi5jb20vd29ybGQvbGl2ZS1uZXdzL2Nvcm9uYXZpcnVzLXBhbmRlbWljLTEyLTA0LTIwLWludGwvaF9hMmI0MGJiNTAxZjJjNGRhM2I0MWIzN2U3YzU2MzZmM9IBVWh0dHBzOi8vYW1wLmNubi5jb20vY25uL3dvcmxkL2xpdmUtbmV3cy9jb3JvbmF2aXJ1cy1wYW5kZW1pYy0xMi0wNC0yMC1pbnRsL2luZGV4Lmh0bWw?oc=5', 'date': 'Fri, 04 Dec 2020 14:22:00 GMT'}....]

