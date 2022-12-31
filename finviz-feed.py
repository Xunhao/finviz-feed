from bs4 import BeautifulSoup
# from datetime import date
import requests
import time  # This will be useful to pause a short while before calling the next ticker

# Interesting Tickers
tickers = ['AAPL']

def scraper(tickers):
	for ticker in tickers:
	    try:
	        finviz = requests.get(f'https://finviz.com/quote.ashx?t={ticker}', headers={'User-Agent': 'Mozilla/5.0'})
	    except Exceptions as e:
	        print(e)
	    else:
	    	# To be initialise for each ticker
	        soup = BeautifulSoup(finviz.content, 'html.parser')
	        news_table = soup.find('table', attrs={"id": "news-table"})
	        news_feed_count = len(news_table.find_all('tr'))
	        latest_ticker_news_date = ''
	        news_count = 0
	        
	        for i in range(news_feed_count):
	        	# i = 18
	        	# The first news link will always contain the latest date and timestamp
	        	# Subsequent links will not have until it reaches the previous day
	        	news_section = news_table.find_all('tr')[i]
	        	news_div_left = news_section.find('div', attrs={'class': 'news-link-left'})
	        	news_div_right = news_section.find('div', attrs={'class':'news-link-right'})

	        	# Key data for each news link
	        	news_td = news_section.find('td').string
	        	news_date_arr = news_td.split(' ')
	        	
	        	# Only assign the date for the first news link which contains the latest date
	        	if i == 0 and len(news_date_arr) == 2:
	        		latest_ticker_news_date = news_date_arr[0]
	        	else:
	        		pass

	        	# This will only be true when we reach the news of the previous date
	        	# As such, we can use this condition to break the loop when it reaches the news of the previous date
	        	if i != 0 and len(news_date_arr) == 2: 
	        		break
	        	else:
	        		news_title = news_div_left.string
		        	news_link = news_div_left.find('a')['href']
		        	news_source = news_div_right.string.strip()

		        	news_count += 1
		        	print(news_count)
		        	print(news_td)
		        	print(news_title)
		        	print(news_link)
		        	print(news_source)
		        	print('\n')

scraper(tickers)