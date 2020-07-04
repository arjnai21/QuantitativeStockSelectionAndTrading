import quandl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
from BasicFunctions import *
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Lines 19-41 adapted from
# https://www.jasonlee.mobi/projects/2018/5/18/building-a-momentum-trading-strategy-using-python

file = list(open("txg01012020to06062020.csv", "r"))
prices = []
dates=[]
for i in range(1, len(file)):
    prices.append(float(file[i].split(",")[4]))
    dates.append(datetime.datetime.strptime(file[i].split(",")[0][1:-1], "%Y-%m-%d"))


print(prices)
# graph_price_2_invest(prices, file="GoldenCrossTXG")
ma_fast = 5
ma_slow = 10

shade_dates = []

trade = ma_trade(prices, ma_fast, ma_slow)
price2invest = price_2_invest(prices, trade,)
ma_fast_values = get_moving_avg(prices, ma_fast)
ma_slow_values = get_moving_avg(prices, ma_slow)
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=90)
locator = mdates.DayLocator(interval=7)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(mdates.DayLocator())



ax.plot(dates, prices, label="Stock price", color="blue")  # price_line
ax.plot(dates, price2invest, label="Holding value", color="black")  # holding_line
ax.plot(dates, ma_slow_values, label="MA " + str(ma_slow), color="green")  # ma_slow_line
ax.plot(dates, ma_fast_values, label="MA " + str(ma_fast), color="red")  # ma_fast_line
ax.legend()
fig.show()
plt.xlabel("Date")
plt.ylabel("Price")
with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\GoldenCrossTXG.pdf') as export_pdf:
    export_pdf.savefig(figure=fig)
    plt.close()



# fig.savefig(file)
# df["MA5"] = df['Close'].rolling(5).mean()
# df["MA20"] = df['Close'].rolling(20).mean()
#
# signals = pd.DataFrame(index=df.index)
# signals['signal'] = 0.0
# signals['MA5'] = df["MA5"]
# signals["MA20"] = df["MA20"]
# signals['signal'][5:] = np.where(signals["MA5"][5:]
#                                  > signals['MA20'][5:], 1.0, 0.0)
#
# signals['positions'] = signals['signal'].diff()
# signals['positions'] = signals['positions'].shift(periods=1)
# fig = plt.figure(figsize=(20, 15))
#
# ax1 = fig.add_subplot(111, ylabel="Price")
#
# df['Close'].plot(ax=ax1)
# df['MA5'].plot(ax=ax1)
# df["MA20"].plot(ax=ax1)
#
#
# ax1.plot(signals.loc[signals.positions == 1.0].index,
#          df.Close[signals.positions == 1.0],
#          marker='o', markersize=10, color='y',
#          linestyle="None")
#
# ax1.plot(signals.loc[signals.positions == -1.0].index,
#          df.Close[signals.positions == -1.0],
#          marker='o', markersize=10, color='y',
#          linestyle="None", markerfacecolor="None")
#
# startInd = -1
#
# for i in range(len(signals['positions'])):
#     if signals['positions'][i] == 1:
#         startInd = i
#
#     if signals['positions'][i] == -1 and startInd != -1:
#         ax1.plot(df["Close"][startInd:i], color='black')
#         startInd = -1
#
#
# plt.legend(loc="best")
# plt.xlabel("Date")
# plt.ylabel("Price")
# with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\FBGoldenCross.pdf') as export_pdf:
#     export_pdf.savefig()
#     plt.close()
