from bs4 import BeautifulSoup
from datetime import date
import requests
import time  # This will be useful to pause a short while before calling the next ticker

# Interesting Tickers
# tickers = ['AAPL']

current_date = date.today()


def scraper():
    try:
        finviz = requests.get(
            'https://finviz.com/quote.ashx?t=AAPL', headers={'User-Agent': 'Mozilla/5.0'})
    except Exceptions as e:
        print(e)
    else:
        soup = BeautifulSoup(finviz.content, 'html.parser')
        news_table = soup.find('table', attrs={"id": "news-table"})
        news_feed_count = len(news_table.find_all('tr'))
        for i in range(news_feed_count):

        	# The first news link will always contain the latest date and timestamp
        	# Subsequent links will not have until it reaches the previous day
        	news_section = news_table.find_all('tr')[i]
        	news_td = news_section.find('td').string
        	news_div_left = news_section.find('div', attrs={'class': 'news-link-left'})
        	news_div_right = news_section.find('div', attrs={'class':'news-link-right'})

        	news_title = news_div_left.string
        	news_link = news_div_left.find('a')['href']
        	news_source = news_div_right.string.strip()

        	print(news_td)
        	print(news_title)
        	print(news_link)
        	print(news_source)

        	break # Use this to break the loop for now

scraper()

'''
        # print(news_table.find('tr', recursive=False).find('td').string)  # This returns the date and time
        print(news_table.find_all('tr')[1])
        # ============== We have to perform these 4 actions every loop ==============
        print(news_table.find_all('tr')[1].find('div', attrs={'class': 'news-link-left'}).string)  # Returns Title
        print(news_table.find_all('tr')[1].find('div', attrs={'class': 'news-link-left'}).find('a')['href'])  # Returns the URL
        
        print(news_table.find_all('tr')[1].find(
            'div', attrs={'class': 'news-link-right'}).string.strip())  # Returns Source
        
        # Attempt to check the presence of a date for every <tr> tag
        # We can check the length of this. If a date is present, arr = 2
        print(news_table.find_all('tr')[1].find('td').string.split(' '))
        # ============== We have to perform these 4 actions every loop ==============

        # This tells us the total number of news feed for a given ticker. We can loop this until the previous date
        # feed_count = len(news_table.find_all('tr'))
        # for i,j in enumerate(range(feed_count)): # For every <tr> tag, we need to check if there's a valid date

'''
