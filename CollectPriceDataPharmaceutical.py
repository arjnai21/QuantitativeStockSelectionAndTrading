from yahoofinancials import YahooFinancials
import csv
import datetime
import os

"""
IMPORTANT

Must first run the program "getStockTickers" in order to have a file named "tickers.txt" in the directory
"""


# stock tickers that have no data
def collectData():
    start_date = "1792-05-17"
    end_date = datetime.date.today().__str__()

    if not os.path.exists('pharmaceutical_data'):
        os.mkdir('pharmaceutical_data')
    print("made directory")
    for line in open("FDADateData.txt"):
        line_arr = line.split(", ")
        if line_arr[1] == "NODATE" or line_arr[2] == "NODATA"or line_arr[2] == "OUTCOME":
            continue
        ticker = line_arr[0]
        print(ticker)
        date = datetime.datetime.strptime(line_arr[1].strip("\n"), "%m/%d/%Y").strftime("%Y-%m-%d")
        # collect historical data for ticker
        financials = YahooFinancials(ticker)
        data = financials.get_historical_price_data(start_date, end_date, "daily")
        prices = data[ticker]["prices"][-91:]

        # header of csv
        ordering = ['distance','date' , 'open', 'close', 'high', 'low', 'volume']
        counter = -90

        # rearrange values with different keys
        for i in range(len(prices)):
            formatted_dict = {}
            for j in ordering:
                if j == 'distance':
                    formatted_dict[j] = counter
                elif j == 'date':
                    formatted_dict[j] = prices[i]['formatted_date']
                else:
                    formatted_dict[j] = prices[i][j]
            prices[i] = formatted_dict
            counter += 1

        keys = prices[0].keys()

        # write prices dictionary to csv file
        with open('pharmaceutical_data/' + ticker + '.csv', 'w', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(prices)

collectData()