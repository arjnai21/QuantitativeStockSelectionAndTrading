import csv
path = "/IEX_historical-prices-master/script/IntradayData03092020-04062020/2020/2020-CW1" # number 1-4, then enter by date(will have to hardcode /DONE/DATA_AAPL.csv

reader = csv.reader(open('filename.csv', 'r'))
d = dict(reader)

#run same moving average test with shorter interval
#figure out data intervals
