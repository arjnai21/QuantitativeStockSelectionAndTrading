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

months = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

ticker = "C"
df = quandl.get('WIKI/' + ticker, api_key="T2K2v57vDVL9Wwx_ia3c")
dates = df["Close"].keys()
trades = []
holds = []

for i in combination_keys:
    performance_dict[i] = []
    trades_dict[i] = ma_trade(df["Close"], i[0], i[1])
    holds_dict[i] = price_2_invest(df["Close"], trades_dict[i])

i = 0
firstDayMarker = 0
largestIndex = 0
while i < len(holds_dict[combination_keys[0]]):
    date = dates[i].to_pydatetime()
    if i != 0 and date.month != dates[i-1].to_pydatetime().month:
        # go from firstDayMarker to i-1
        for j in combination_keys:
            hold_value_at_end_of_month = holds_dict[j][i-1]
            hold_value_at_start_of_month = holds_dict[j][firstDayMarker]
            performance = ((hold_value_at_end_of_month - hold_value_at_start_of_month) / hold_value_at_start_of_month) * 100  # percentage
            performance_dict[j].append(performance)
            if performance > 800:
                largestIndex = i
        firstDayMarker = i
    i += 1
print(max(performance_dict[(10, 20)]))
print(performance_dict[(10, 20)].index((max(performance_dict[(10, 20)]))))
#print(len(dates))
print(dates[largestIndex])
print(largestIndex / 20)
print(holds_dict)
# print(dates[int(performance_dict[(10, 20)].index((max(performance_dict[(10, 20)]))) * (365/12))])
#graphing
fig = plt.figure(figsize=(20, 3))
ax = fig.add_subplot(111)
for i in performance_dict.keys():
    ax.plot(performance_dict[i], label=str(i))

days = len(performance_dict[combination_keys[0]])
fig.legend()
fig.show()
fig.savefig('MovingAverageTestContinuousMay')
# with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\MovingAverageTestContinuous.pdf') as export_pdf:
#     export_pdf.savefig(fig)
#     plt.close()
