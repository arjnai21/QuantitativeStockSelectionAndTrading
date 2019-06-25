from yahoofinancials import YahooFinancials
import csv
import time

# ZAZZT not working
financials = YahooFinancials("ZAZZT")
print(financials.get_stock_data())
financials = YahooFinancials("AAPL")
print(financials.get_stock_data())
for ticker in open("tickers.txt"):
    ticker = ticker.strip('\n')
    print(ticker)
    financials = YahooFinancials(ticker)
    start = time.time()
    data = financials.get_historical_price_data("2019-01-01", "2019-06-24", "daily")
    prices = data[ticker]["prices"]
    ordering = ['high', 'low', 'open', 'close', 'volume', 'adjclose']
    for i in range(len(prices)):
        newdic = {}
        newdic['Date'] = prices[i]['formatted_date']
        for j in ordering:
            newdic[ticker + "." + j.title()] = prices[i][j]
        prices[i] = newdic
        del newdic

    keys = prices[0].keys()

    with open('data/' + ticker + '.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()

        dict_writer.writerows(prices)
