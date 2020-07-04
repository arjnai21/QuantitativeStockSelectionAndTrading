import calendar
import datetime
import quandl
from matplotlib.backends.backend_pdf import PdfPages
from BasicFunctions import *
import matplotlib.pyplot as plt
import numpy


moving_averages = [5, 10, 15, 20]
combination_keys = [(moving_averages[i], moving_averages[j]) for i in range(len(moving_averages)) for j in range(i+1, len(moving_averages))]
combination_dict = {}
for i in combination_keys:
    combination_dict[i]= []
months = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

ticker = "C"
df = quandl.get('WIKI/' + ticker, api_key="T2K2v57vDVL9Wwx_ia3c")

# make it continuous dont start over each month
# run it over whole month and then check stats
# also run s&p 500
# for each combination graph the curve for portfolio value
# for each combination send the portfolio value curve
# combination map to vector of portfolio value
# calculate annualized return for a bunch of stuff
# graph show plot as annualized return
best_yearly_performances = []
best_yearly_averages = []
best_total_averages = []
best_total_performances = []
for year in range(1977, 2018):
    best_yearly_performance = -float('inf')
    best_yearly_config = []
    best_monthly_performances = []
    best_monthly_averages = []
    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]
        dataset = df["Close"][datetime.date(year, month, 1):datetime.date(year, month, last_day)]
        best_monthly_performance = -float('inf')
        best_monthly_config = []
        for i in range(len(moving_averages)-1):
            for j in range(i+1, len(moving_averages)):
                trade = ma_trade(dataset, moving_averages[i], moving_averages[j])
                hold = price_2_invest(dataset, trade)
                performance = ((hold[-1] - hold[0]) / hold[0]) * 100  # percentage
                combination_dict[(moving_averages[i], moving_averages[j])].append(performance)
                if performance > best_monthly_performance:
                    best_monthly_performance = performance
                    best_monthly_config = [moving_averages[i], moving_averages[j]]

        # end of a month
        if best_monthly_performance > best_yearly_performance:
            best_yearly_performance = best_monthly_performance
            best_yearly_config = best_monthly_config
        best_monthly_performances.append(best_monthly_performance)
        best_monthly_averages.append(best_monthly_config)
        print(months[month] + " " + str(year) + ":")
        print("\tBest Configuration:\n\tma_fast: " + str(best_monthly_config[0]) + "\n\tma_slow: " + str(best_monthly_config[1]))
        print("Best Performance: " + str(best_monthly_performance) + "%\n\n")

    # end of a year

    print(str(year) + " Best: ")
    print("\tBest Configuration:\n\tma_fast: " + str(best_yearly_config[0]) + "\n\tma_slow: " + str(
        best_yearly_config[1]))
    print("Best Performance: " + str(best_yearly_performance) + "%\n\n")
    best_total_averages.append(best_monthly_averages)
    best_total_performances.append(best_monthly_performances)
    best_yearly_performances.append(best_yearly_performance)
    best_yearly_averages.append(best_yearly_config)

#graphing
fig = plt.figure(figsize=(20, 3))
ax = fig.add_subplot(111)
for i in combination_dict.keys():
    ax.plot(combination_dict[i], label=str(i))

days = len(combination_dict[combination_keys[0]])
plt.legend()
plt.xticks(range(0, days, 10))
# plt.figure(figsize=(20, 2))
# plt.tight_layout()
plt.show()
# with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\MovingAverageTest.pdf') as export_pdf:
#     export_pdf.savefig(fig)
#     plt.close()

"""
best yearly performances:
list containing the largest percent gain in each year
as many elements(floats) as there are years
best yearly averages:
list containing the best configuration of averages for each year
as many elements(lists representing configuration) as there are years
best total averages:
list containing lists of the best configuration for each month (as many lists as there are years, with each list containing twelve lists of length 2 for the averages)
best total performances:
list containing lists of the best performances for each month (as many lists as there are years, with each list containing a list of length 12 for the performances)

NOTE:
best yearly performances should select the max of each of the yearly lists in best total averages
best yearly averages should select the best of each of the yearly lists in best total averages, which correspond to the best performances for that year
"""

