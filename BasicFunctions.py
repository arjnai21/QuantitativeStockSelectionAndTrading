# def yr_vol(val, daily_scale=252):
#
# def yr_rtn(val, daily_scale=252):
#
# def max_drawdn(val):
#
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
trade = ma_trade(data)
print(price2invest(data, trade, 1000))