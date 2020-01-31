import calendar
import datetime
import quandl
from matplotlib.backends.backend_pdf import PdfPages
from BasicFunctions import *
import matplotlib.pyplot as plt
import numpy
import pandas as pd

moving_averages = (5, 10, 15, 20)
combination_keys = [(moving_averages[i], moving_averages[j]) for i in range(len(moving_averages)) for j in range(i+1, len(moving_averages))]
performance_dict = {}
holds_dict = {}
trades_dict = {}
for i in combination_keys:
    performance_dict[i] = []

months = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

ticker = "C"
df = quandl.get('WIKI/' + ticker, api_key="T2K2v57vDVL9Wwx_ia3c")
dates = df["Close"].keys()
trades = []
holds = []

for i in combination_keys:
    trades_dict[i] = ma_trade(df["Close"], i[0], i[1])
    holds_dict[i] = price_2_invest(df["Close"], trades_dict[i])

i = 0
firstDayMarker = 0
while i < len(holds_dict[combination_keys[0]]):
    date = dates[i].to_pydatetime()
    if i != 0 and date.month != dates[i-1].to_pydatetime().month:
        print("performing calculation")
        # go from firstDayMarker to i-1
        for j in combination_keys:
            performance = ((holds_dict[j][i-1] - holds_dict[j][firstDayMarker]) / holds_dict[j][firstDayMarker]) * 100  # percentage
            hold_value_at_end_of_month = holds_dict[j][i-1]
            hold_value_at_start_of_month = holds_dict[j][firstDayMarker]
            performance_dict[j].append(performance)
        firstDayMarker = i
    i += 1

#graphing
fig = plt.figure(figsize=(20, 3))
ax = fig.add_subplot(111)
for i in performance_dict.keys():
    ax.plot(performance_dict[i], label=str(i))

days = len(performance_dict[combination_keys[0]])
plt.legend()
plt.show()
with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\MovingAverageTestContinuous.pdf') as export_pdf:
    export_pdf.savefig(fig)
    plt.close()
