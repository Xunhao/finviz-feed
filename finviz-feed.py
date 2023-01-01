from bs4 import BeautifulSoup
import requests
import time
import csv
import os

# Tickers
tickers = ['AAPL', 'COST']


def scraper(tickers):
    # Create a csv file to hold the scrapped data for all tickers
    current_directory = os.getcwd()
    with open(f'{current_directory}/finviz_feed.csv', 'w') as finviz_feed:
        finviz_feed_header = ['Date Time', 'Ticker',
                              'News Title', 'News Link', 'News Source']
        finviz_feed_data = []
        writer = csv.writer(finviz_feed)
        writer.writerow(finviz_feed_header)

        for ticker in tickers:
            try:
                finviz = requests.get(
                    f'https://finviz.com/quote.ashx?t={ticker}', headers={'User-Agent': 'Mozilla/5.0'})
            except Exceptions as e:
                print(e)
            else:
                # To be initialised for each ticker
                soup = BeautifulSoup(finviz.content, 'html.parser')
                news_table = soup.find('table', attrs={"id": "news-table"})
                news_feed_count = len(news_table.find_all('tr'))
                news_latest_date = ''
                news_count = 0  # We can consider return this in as an output to indicate the success of the script

                for i in range(news_feed_count):
                    # The first news link of the day will always contain both date and time. Subsequent links will not have until it reaches the previous day
                    # Prepare the tags to scrap
                    news_section = news_table.find_all('tr')[i]
                    news_div_left = news_section.find(
                        'div', attrs={'class': 'news-link-left'})
                    news_div_right = news_section.find(
                        'div', attrs={'class': 'news-link-right'})

                    # Key data for each news link
                    news_td = news_section.find('td').string
                    news_date_arr = news_td.split(' ')

                    if len(news_date_arr) == 2:  # Only true when it includes both date and time
                        # Assign the date when it does exist
                        news_latest_date = news_date_arr[0]
                        news_date_time = news_td
                    else:
                        news_date_time = f'{news_latest_date} {news_td}'

                    # This will only be true when we reach the news of the previous date
                    if i != 0 and len(news_date_arr) == 2:
                        break  # Move to the next ticker
                    else:
                        news_title = news_div_left.string  # Assign news title
                        news_link = news_div_left.find(
                            'a')['href']  # Assign news link
                        news_source = news_div_right.string.strip()  # Assign news source

                        finviz_feed_data.append(
                            [news_date_time, ticker, news_title, news_link, news_source])

                        news_count += 1

                print(f'{news_count} news found for {ticker}')

        time.sleep(2)  # Pause between tickers
        # Append data into csv file after accumulating the data for all tickers
        writer.writerows(finviz_feed_data)


scraper(tickers)
