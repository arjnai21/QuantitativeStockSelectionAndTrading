from oldstuff.CollectPriceData import collectData
from oldstuff.GetStockTickers import getTickers

"""
This file completes the entire task

IMPORTANT: It is necessary to install the yahoofinancials API, which can be done simply with the command

pip install yahoofinancials

Creates a folder in the working directory titled 'data', and writes all the .csv files for each ticker to it

"""


def main():
    getTickers()
    collectData()


main()

