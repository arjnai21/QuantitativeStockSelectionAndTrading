from CollectPriceData import collectData
from GetStockTickers import getTickers

"""
This file completes the entire task

Creates a folder in the working directory titled 'data', and writes all the .csv files for each ticker to it

"""


def main():
    getTickers()
    collectData()


main()

