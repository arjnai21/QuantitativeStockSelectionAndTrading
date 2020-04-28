import quandl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime

ticker = "C"
df = quandl.get('WIKI/' + ticker, api_key="T2K2v57vDVL9Wwx_ia3c")
date = str(datetime.date(2011, 4, 7))
date2 = str(datetime.date(2011, 6, 15))
print(type(df["Close"][date]))
may_data = df["Close"][date:date2]

df["Close"] = 1
print(may_data)
ma5 = may_data.rolling(15).mean()
ma10 = may_data.rolling(20).mean()
print(ma10["2011-05-06"])
print(ma5["2011-05-06"])
print(ma10["2011-05-09"])
print(ma5["2011-05-09"])

with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\CMovingAverage1520.pdf') as export_pdf:
    may_data.plot(label="Price")
    ma5.plot(label="MA15")
    ma10.plot(label="MA20")
    plt.legend(loc=4)
    plt.xlabel("Date")
    plt.ylabel("$")
    export_pdf.savefig()
    plt.close()
print("done")
