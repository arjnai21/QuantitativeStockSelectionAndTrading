import statistics
import math
def yr_vol(val, daily_scale=252):
    daily_percent_change = [((val[i] - val[i-1]) / val[i-1]) for i in range(1, len(val))]
    return statistics.pstdev(daily_percent_change) * math.sqrt(daily_scale)
#
# def yr_rtn(val, daily_scale=252):
#
def max_drawdn(val):
    peaks = [0]
    peak_val = val[0]
    for i in range(1, len(val)-1):
        if val[i] > peak_val and val[i] > val[i+1]:
            peak_val = val[i]
            peaks.append(i)
    peaks.append(len(val) + 1) # slicing purposes
    max_drawdn = 0
    for i in range(len(peaks)-1):
        testing = val[peaks[i]:peaks[i+1]]
        drawdn = val[peaks[i]] - min(val[peaks[i]:peaks[i+1]]) # search from peak to peak for minum
        if drawdn > max_drawdn:
            max_drawdn = drawdn
            print(max_drawdn)

    return max_drawdn # CURRENTLY PRICE DROP NOT PERCENTAGE




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


def price2invest(price, i_hold, cash=-1):
    if cash == -1:
        cash = price[1]
    num_shares = 0
    i = 0
    for i in range(len(price)):
        if i_hold[i] == 0 and i !=0 and i_hold[i-1] == 1:
            cash = num_shares * price[i]
            num_shares = 0
        if i_hold[i] == 1 and (i == 0 or i_hold[i-1] == 0):
            num_shares = cash / price[i]
            cash = 0

    return cash + num_shares * price[-1]



def read_stock_into_list(filename):
    with open(filename) as f:
        lines = [float(i) for i in f.readlines()]
    return lines

data = read_stock_into_list("StockX.txt")
print(min(data))
trade = ma_trade(data)
print(price2invest(data, trade, 46570))
print(yr_vol(data))
print(max_drawdn(data))