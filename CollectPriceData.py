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
    not_working = ["ZAZZT", "ZBZZT", "ZXYZ.A", "BRPM.U", "CBX",  "FPAC.W", "GIG.R", "GIG.W", "GIX.U", "GRAF.U", "GSAH.W",
                   "IAA.V", "IBO", "IGZ", "LGC.U", "LGC.W", "MFAC.W", "MOSC.U", "NTEST.C", "PVT.U", "PVT.W", "RMG.W",
                   "SHLL.U", "SPAQ.U", "TRNE.W", "TRNO", "VST.A", "ZTEST"]

    # stock tickers that have a '.' but who's YahooFinancials call requires a '-' instead
    not_right = ["AGM.A", "AKO.A", "AKO.B", "BF.A", "BF.B", "BH.A", "BIO.B", "BRK.A", "BRK.B", "BWL.A", "CBS.A", "CRD.A",
                 "CRD.B", "CWEN.A", "GEF.B", "GTN.A", "HEI.A", "HVT.A", "JW.A", "JW.B", "MKC.V", "MOG.A", "MOG.B", "STZ.B",
                 "TAP.A", "WSO.B"]

    start_date = "2019-01-01"
    end_date = datetime.date.today().__str__()

    if not os.path.exists('data'):
        os.mkdir('data')

    for ticker in open("tickers.txt"):
        ticker = ticker.strip('\n')
        if ticker in not_right:
            ticker = ticker.replace('.', '-')

        # if ticker has no data. All tickers that begin with 'ATEST' have no data
        if ticker in not_working or ticker[:5] == "ATEST":
            print("skipped")
            continue

        # collect historical data for ticker
        financials = YahooFinancials(ticker)
        data = financials.get_historical_price_data(start_date, end_date, "daily")
        prices = data[ticker]["prices"]

        # header of csv
        ordering = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adjclose']

        # rearrange values with different keys
        for i in range(len(prices)):
            formatted_dict = {'Date': prices[i]['formatted_date']}
            for j in ordering:
                formatted_dict[ticker + "." + j] = prices[i][j.lower()]
            prices[i] = formatted_dict

        keys = prices[0].keys()


        # write prices dictionary to csv file
        with open('data/' + ticker + '.csv', 'w', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(prices)


