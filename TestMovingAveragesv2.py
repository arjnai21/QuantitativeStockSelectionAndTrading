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
print(df["Close"][0])
print(type(df["Close"].keys()[0]))
dates = df["Close"].keys()
print(type(dates[0]))
print(type(dates[0].to_pydatetime()))
print(type(dates[0]))
trades = []
holds = []

for i in combination_keys:
    trades_dict[i] = ma_trade(df["Close"], i[0], i[1])
    holds_dict[i] = price_2_invest(df["Close"], trades_dict[i])

firstDayCounter = 0
firstDays = pd.date_range('1/1/1977', '12/1/2019', freq='BMS')
firstMonth = 1
firstYear = 1977
i = 0 # first day of month
firstDayMarker = 0
while i < len(holds_dict[combination_keys[0]]):

    date = dates[i].to_pydatetime()
    print(date)
    month = date.month
    year = date.year
    first_day = date.day
    if i != 0 and month != dates[i-1].to_pydatetime().month:
        print("performing calculation")
        # go from firstDayMarker to i-1
        for j in combination_keys:
            performance = ((holds_dict[j][i-1] - holds_dict[j][firstDayMarker]) / holds_dict[j][firstDayMarker]) * 100  # percentage
            hold_value_at_end_of_month = holds_dict[j][i-1]
            hold_value_at_start_of_month = holds_dict[j][firstDayMarker]
            if performance > 100:
                x = 0
            performance_dict[j].append(performance)

        firstDayMarker = i
    i+=1

x = 0
print(max(performance_dict[(10, 20)]))
#graphing
fig = plt.figure(figsize=(20, 3))
ax = fig.add_subplot(111)
for i in performance_dict.keys():
    ax.plot(performance_dict[i], label=str(i))

days = len(performance_dict[combination_keys[0]])
plt.legend()
plt.xticks(range(0, days, 10))
# plt.figure(figsize=(20, 2))
# plt.tight_layout()
plt.show()
with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\MovingAverageTestContinuous.pdf') as export_pdf:
    export_pdf.savefig(fig)
    plt.close()


    # last_day: object = (firstDays[firstDayCounter + 1] - datetime.timedelta(days=1)).day
    #
    # # range is i to i + last day - first day
    # for j in combination_keys:
    #     performance = ((holds_dict[j][i+last_day-first_day] - holds_dict[j][i]) / holds_dict[j][i]) * 100  # percentage
    #     performance_dict[j].append(performance)
    #     # calc performance for i
    #     # append to combination_dict for performances
    # # at start of next loop, i add last_day - day
    # firstDayCounter += 1
    # print(i)
    # print(dates[i])
    # print(firstDays[firstDayCounter])
    #
    # while not (dates[i] == firstDays[firstDayCounter]):
    #
    #     i += 1
    # # i += last_day - first_day
    # # check = dates[i]
    # # othercheck = firstDays[firstDayCounter]
    # assert dates[i] == firstDays[firstDayCounter]






# make it continuous dont start over each month
# run it over whole month and then check stats
# also run s&p 500
# for each combination graph the curve for portfolio value
# for each combination send the portfolio value curve
# combination map to vector of portfolio value
# calculate annualized return for a bunch of stuff
# graph show plot as annualized return
# best_yearly_performances = []
# best_yearly_averages = []
# best_total_averages = []
# best_total_performances = []
# for year in range(1977, 2018):
#     best_yearly_performance = -float('inf')
#     best_yearly_config = []
#     best_monthly_performances = []
#     best_monthly_averages = []
#     for month in range(1, 13):
#         last_day = calendar.monthrange(year, month)[1]
#         dataset = df["Close"][datetime.date(year, month, 1):datetime.date(year, month, last_day)]
#         best_monthly_performance = -float('inf')
#         best_monthly_config = []
#         for i in range(len(moving_averages)-1):
#             for j in range(i+1, len(moving_averages)):
#
#                 performance = ((hold[-1] - hold[0]) / hold[0]) * 100  # percentage
#                 performance_dict[(moving_averages[i], moving_averages[j])].append(performance)
#                 if performance > best_monthly_performance:
#                     best_monthly_performance = performance
#                     best_monthly_config = [moving_averages[i], moving_averages[j]]
#
#         # end of a month
#         if best_monthly_performance > best_yearly_performance:
#             best_yearly_performance = best_monthly_performance
#             best_yearly_config = best_monthly_config
#         best_monthly_performances.append(best_monthly_performance)
#         best_monthly_averages.append(best_monthly_config)
#         print(months[month] + " " + str(year) + ":")
#         print("\tBest Configuration:\n\tma_fast: " + str(best_monthly_config[0]) + "\n\tma_slow: " + str(best_monthly_config[1]))
#         print("Best Performance: " + str(best_monthly_performance) + "%\n\n")
#
#     # end of a year
#
#     print(str(year) + " Best: ")
#     print("\tBest Configuration:\n\tma_fast: " + str(best_yearly_config[0]) + "\n\tma_slow: " + str(
#         best_yearly_config[1]))
#     print("Best Performance: " + str(best_yearly_performance) + "%\n\n")
#     best_total_averages.append(best_monthly_averages)
#     best_total_performances.append(best_monthly_performances)
#     best_yearly_performances.append(best_yearly_performance)
#     best_yearly_averages.append(best_yearly_config)
#
# #graphing
# fig = plt.figure(figsize=(20, 3))
# ax = fig.add_subplot(111)
# for i in performance_dict.keys():
#     ax.plot(performance_dict[i], label=str(i))
#
# days = len(performance_dict[combination_keys[0]])
# plt.legend()
# plt.xticks(range(0, days, 10))
# # plt.figure(figsize=(20, 2))
# # plt.tight_layout()
# plt.show()
# # with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\MovingAverageTest.pdf') as export_pdf:
# #     export_pdf.savefig(fig)
# #     plt.close()
#
# """
# best yearly performances:
# list containing the largest percent gain in each year
# as many elements(floats) as there are years
# best yearly averages:
# list containing the best configuration of averages for each year
# as many elements(lists representing configuration) as there are years
# best total averages:
# list containing lists of the best configuration for each month (as many lists as there are years, with each list containing twelve lists of length 2 for the averages)
# best total performances:
# list containing lists of the best performances for each month (as many lists as there are years, with each list containing a list of length 12 for the performances)
#
# NOTE:
# best yearly performances should select the max of each of the yearly lists in best total averages
# best yearly averages should select the best of each of the yearly lists in best total averages, which correspond to the best performances for that year
# """
#
