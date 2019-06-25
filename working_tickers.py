from yahoofinancials import YahooFinancials

x = 0
file = open("working_tickers.txt", "w")
for i in open("tickers.txt"):
    i = i.strip("\n")
    financials = YahooFinancials(i)
    avg = financials.get_50day_moving_avg()
    if avg is not None:
        file.write(i + '\n')

    x += 1
print("Process finished with this many valid stocks : " + x)
file.close()
