import statistics
import matplotlib.pyplot as plt
import math


def yr_vol(val, daily_scale=252):
    daily_percent_change = [((val[i] - val[i-1]) / val[i-1]) for i in range(1, len(val))]
    return statistics.pstdev(daily_percent_change) * math.sqrt(daily_scale)

def yr_rtn(val, daily_scale=252):
    cum_rtn = (val[-1] - val[0]) / val[0]
    return (1+cum_rtn) ** (365/len(val)) - 1


def max_drawdn(val):
    peaks = [0]
    peak_val = val[0]
    for i in range(1, len(val)-1):
        if val[i] > peak_val and val[i] > val[i+1]:
            peak_val = val[i]
            peaks.append(i)
    peaks.append(len(val) + 1)  # slicing purposes
    max_drawdown = 0
    for i in range(len(peaks)-1):
        drawdn = (val[peaks[i]] - min(val[peaks[i]:peaks[i+1]])) / val[peaks[i]] # search from peak to peak for minimum
        if drawdn > max_drawdown:
            max_drawdown = drawdn

    return max_drawdown


def ma_trade(price, ma_fast=5, ma_slow=10):
    ret = []
    for i in range(ma_slow):
        ret.append(0)
    for i in range(ma_slow, len(price)):
        fast_avg = sum(price[i-ma_fast:i]) / ma_fast
        slow_avg = sum(price[i-ma_slow:i]) / ma_slow
        if fast_avg > slow_avg:
            ret.append(1)
        else:
            ret.append(0)
    return ret


def price_2_invest(price, i_hold, cash=-1):
    if cash == -1:
        cash = price[0]
    values = []
    num_shares = 0
    for i in range(len(price)):
        if i_hold[i] == 0 and i !=0 and i_hold[i-1] == 1:
            cash = num_shares * price[i]
            num_shares = 0
        if i_hold[i] == 1 and (i == 0 or i_hold[i-1] == 0):
            num_shares = cash / price[i]
            cash = 0
        values.append(cash + num_shares * price[i])

    return values


def read_stock_into_list(filename):
    with open(filename) as f:
        lines = [float(i) for i in f.readlines()]
    return lines

def get_moving_avg(price, freq):
    ma = [None for i in range(freq)]
    for i in range(freq, len(price)):
        ma.append(sum(price[i-freq:i]) / freq)
    return ma


def graph_price_2_invest(price, ma_fast=5, ma_slow=10, cash=-1):
    trade = ma_trade(price, ma_fast, ma_slow)
    price2invest = price_2_invest(price, trade, cash)
    ma_fast_values = get_moving_avg(price, ma_fast)
    ma_slow_values = get_moving_avg(price, ma_slow)
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(price, label="Stock price", color="blue")  # price_line
    ax.plot(price2invest, label="Holding value", color="black")  # holding_line
    ax.plot(ma_slow_values, label="MA_Slow", color="green")  # ma_slow_line
    ax.plot(ma_fast_values, label="MA Fast", color="red")  # ma_fast_line
    ax.legend()
    fig.show()


data = read_stock_into_list("StockX.txt")
# randomly generated list of 1s and 0s
hold = [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
print(yr_vol(data))
print(yr_rtn(data))
print(max_drawdn(data))
print(ma_trade(data))
print(price_2_invest(data, hold))
graph_price_2_invest(data)



