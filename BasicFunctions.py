# def yr_vol(val, daily_scale=252):
#
# def yr_rtn(val, daily_scale=252):
#
# def max_drawdn(val):
#
# def ma_trade(price, ma_fast=5, ma_slow=10):
#
# def price2invest(price, i_hold, cash=-1):
#     if cash == -1:
#         cash = price[1]

def read_stock_into_list(filename):
    with open(filename) as f:
        lines = [float(i) for i in f.readlines()]
    return lines

print(read_stock_into_list("StockX.txt"))