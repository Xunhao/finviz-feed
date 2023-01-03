# finviz-feed

## Project Details

### Description
This project utilises **Beautiful Soup** to web scrap the [finviz](www.finviz.com) website for news related to various stocks. I choose finviz because the website has already done a great job in aggregating news and also because it is a financial website that I use to keep myself updated about my portfolio. The script would scrap the news for various tickers as specified in an array. Once the data has been scrapped, it would be stored in a csv file for ease of reference. The script has been built with the intention to be triggered daily since it would only scrap the latest news.

### Libraries
1. Beautiful Soup
2. Requests

### Motivation
At times, I find it challenging to keep myself updated with the latest news for stocks that I am currently holding. So I decided to build a script that fetches the news, something like a RSS feed, and send them to me instead of having to search through the website ticker by ticker. With this automation, I no longer have to visit finviz on a daily basis to get news update. 

### How to use
1. Download the necessary libraries
2. Update the tickers variable with the stocks that you are interested in

If the script is successful, you should see a csv file, **finviz_feed.csv**, being created in the same directory containing the tickers that you have specified and the latest news scrapped.

### Future Possible Enhancements
1. Automatically open the csv file with an spreadsheet application, Excel or Numbers upon completion.
2. Inclusion of high-level metrics for each ticker such as - % Price Change, Prev Close, Prev Open, 52-week High vs Low etc.

### Limitations
1. Only scrap the latest news (Intentionally designed this way but may be viewed as a limitation to some).

## Credits
1. [finviz](www.finviz.com)
    - finviz is a great website to get daily updates about the stock market. The service is packed with features that are relevant to both long-term investors and traders alike. I highly recommend checking out the website and leverage what is relevant for you. If you find it useful, consider subscribing for their service! 
