import xlsxwriter
from yahoofinancials import YahooFinancials
import datetime
from dateutil.relativedelta import relativedelta
from BasicFunctions import *
import quandl

file = list(open("FDA_data20182019.csv"))

workbook = xlsxwriter.Workbook('BaselinePharmaceuticalPerformance.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_row(0, 0,
                    "Ticker PDUFA_date Drug Entry.date Entry.closePrice Exit.date Exit.closePrice Return maxDrawdown AnnualizedRtn AnnualizedVolatility".split())

for i in range(1, len(file)):
    line = file[i].strip("\n").split(',')
    ticker = line[0]
    drug = line[1]
    drug_date = datetime.datetime.strptime(line[2], "%m/%d/%Y")
    print(ticker)

    start_date = (drug_date - relativedelta(months=2)).strftime("%Y-%m-%d")

    drug_date = drug_date.strftime("%Y-%m-%d")

    print(line)
    financials = YahooFinancials(ticker)
    print("got financials")
    # data = quandl.get("EOD/" + ticker, start_date=start_date, end_date = drug_date, api_key="T2K2v57vDVL9Wwx_ia3c")
    data = financials.get_historical_price_data(start_date, drug_date, "daily")
    print("got price data")
    if data[ticker] is None or "prices" not in data[ticker].keys():
        print(ticker + " is not available")
        continue
    prices = data[ticker]["prices"]
    price_arr = []
    for entry in prices:
        if (entry["close"]) is None:
            print("incomplete data")
            continue
        price_arr.append(entry["close"])
    entry_date = prices[0]["formatted_date"]
    exit_date = prices[-1]["formatted_date"]
    entry_close_price = price_arr[0]
    exit_close_price = price_arr[-1]
    # trade = [1 for i in range(len(price_arr))]
    hold = price_arr
    performance = (hold[-1] - hold[0]) / hold[0]

    max_drawdown = max_drawdn(hold)
    annualized_return = yr_rtn(hold)
    annualized_volatility = yr_vol(hold)
    row = [ticker, drug, drug_date, entry_date, entry_close_price, exit_date, exit_close_price, performance,
           max_drawdown, annualized_return, annualized_volatility]
    print(row, "\n\n")
    print(type(i))
    worksheet.write_row(i, 0, row)

workbook.close()
