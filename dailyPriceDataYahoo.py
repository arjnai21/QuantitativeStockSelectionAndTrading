from yahoofinancials import YahooFinancials
import csv

for i in range(5):
    for ticker in open("tickers.txt"):
        ticker = ticker.strip('\n')
        financials = YahooFinancials(ticker)
        data = financials.get_historical_price_data("2019-01-01", "2019-06-24", "daily")
        prices = data[ticker]["prices"]
        ordering = ['date', 'high', 'low', 'open', 'close', 'volume', 'adjclose']
        for i in range(len(prices)):
            newdic = {}
            for j in ordering:
                if j == 'date':
                    newdic['Date'] = prices[i]['formatted_date']
                else:
                    newdic[ticker + "." + j.title()] = prices[i][j]

            prices[i] = newdic
            del newdic

        keys = prices[0].keys()

        with open('data/' + ticker + '.csv', 'w', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()

            dict_writer.writerows(prices)
