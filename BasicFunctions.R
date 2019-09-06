yr.vol<- function(val, daily.scale=252) {
   #this function calculates/returns Annualized Volatility
   #see https://www.fool.com/knowledge-center/how-to-calculate-annualized-volatility.aspx
   #val: a vector of the value of a portfolio/equity over n time points
   #daily.scale: assume there are daily.scale trading days in a year when computing the Annualized Volatility
}

yr.rtn<- function(val, daily.scale=252) {
   #this function calculates/returns Annualized Return
   #see https://www.investopedia.com/terms/a/annualized-total-return.asp
   #val: a vector of the value of a portfolio/equity over n time points
   #daily.scale: assume there are daily.scale trading days in a year when computing the Annualized Return
}

max.drawdn<- function(val) {
   #this function calculates/returns Maximum Drawdown 
   #see https://blogs.cfainstitute.org/investor/2013/02/12/sculpting-investment-portfolios-maximum-drawdown-and-optimal-portfolio-strategy/
   #val: a vector of the value of a portfolio/equity over n time points
}

ma.trade <- function(price, ma_fast=5, ma_slow=10) {
#price: a vector of stock price over n time points
#ma_fast: an integer to indicate the fast simple moving average of ma_fast time points
#ma_fast: an integer to indicate the slow simple moving average of ma_slow time points
#this function implement a simple strategy: buy when there is a golden cross, and sell when there is a death cross
#return value: i.hold a vector of indicator over n time points, 0 means not hold the stock, 1 means hold
}

price2invest<- function(price, i.hold, cash=price[1]) {
#price: a vector of stock price over n time points
#i.hold: a vector of indicator over n time points, 0 means not hold the stock, 1 means hold
#cash: the initial cash amount, the default value is the value of price at day 1 (price[1])
# Example: 0011100110 two holding periods, hold1: buy at 3rd time point and sell and 5th; hold2: buy at 8th, and sell at 9th.
#return value: equity.val, a vector of equity value over n time points, 0 means not hold the stock, 1 means hold
# (1)buy #shares = cash/price[buy.date], which can be numberical and can be also <1
# (2)sell all shares that are in hold at price[sell.date]
# (3)During the nonholding period, holding cash and its value remains constant during the nonholding period
# (4)During the holding period, the equity value will flucturate with the price at the same % of increase/descrease
}