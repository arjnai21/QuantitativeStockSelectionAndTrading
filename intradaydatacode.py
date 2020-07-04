# readings take place once per minute, unless there's gap in data
from BasicFunctions import ma_trade, price_2_invest
import matplotlib.pyplot as plt
import csv

# path = r"IEX_historical-prices-master/script/IntradayData03092020-04062020/2020/2020-CW1" # number 1-4, then enter by date(will have to hardcode /DONE/DATA_AAPL.csv
# reader = csv.reader(open('filename.csv', 'r'))
# d = dict(reader)
dateCounter = 0
# minutes
moving_averages = (5, 10, 15, 20)
combination_keys = [(moving_averages[i], moving_averages[j]) for i in range(len(moving_averages)) for j in
                    range(i + 1, len(moving_averages))]
performance_dict = {}
for i in combination_keys:
    performance_dict[i] = []
dates = []
for i in range(1, 6):

    if i == 1:
        dates = [str(j) for j in range(20200309, 20200314)]
    elif i == 2:
        dates = [str(j) for j in range(20200316, 20200320)]
    elif i == 3:
        dates = [str(j) for j in range(20200323, 20200328)]
    elif i == 4:
        dates = ["20200330", "20200331", "20200401", "20200402", "20200403"]
    elif i == 5:
        dates = ["20200406"]
    for j in dates:
        path = r"IEX_historical-prices-master/script/IntradayData03092020-04062020/2020/2020-CW1" \
               + str(i) + "/" + j + "/DONE/" + j + "_AAPL.csv"
        file = list(open(path, 'r'))
        close_prices = []
        for k in range(1, len(file)):
            line = file[k].split(",")
            if line[7] != '':
                close_prices.append(float(line[7]))
        # print(close_prices)
        for k in combination_keys:
            trade_values = ma_trade(close_prices, k[0], k[1])
            hold_values = price_2_invest(close_prices, trade_values)
            print(hold_values)
            print("\n\n\n")
            daily_performance = 100 * (hold_values[-1] - hold_values[0]) / hold_values[0]
            performance_dict[k].append(daily_performance)
        x = 00


fig = plt.figure()
ax = fig.add_subplot(111)
for i in performance_dict.keys():
    ax.plot(performance_dict[i], label=str(i))
ax.set_title("Daily Performance")
fig.legend()
fig.savefig("AAPL Daily Performance")
fig.show()

# htgfv

# run same moving average test with shorter interval
# figure out data intervals
