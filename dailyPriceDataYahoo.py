from yahoofinancials import YahooFinancials
import csv

financials = YahooFinancials('AAPL')
x = financials.get_historical_price_data("2019-01-01", "2019-06-24", "daily")
val = x['AAPL']["prices"]
ordering = ['date', 'high','low','open','close','volume','adjclose']
for i in range(len(val)):
    newdic = {}
    for j in ordering:
        if j == 'date':
            newdic[j] = val[i]['formatted_date']
        else:
            newdic[j] = val[i][j]

    val[i] = newdic
    del newdic

keys = val[0].keys()


with open('aapl.csv', 'w') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()

    dict_writer.writerows(val)
print(financials.get_historical_price_data("2019-01-01", "2019-06-24", "daily"))
