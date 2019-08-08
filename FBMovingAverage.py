import quandl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df = quandl.get('WIKI/FB')
df["MA5"] = df['Close'].rolling(5).mean()
df["MA10"] = df['Close'].rolling(10).mean()
with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelection\FBMovingAverage.pdf') as export_pdf:
    df['Close'].plot()
    df['MA5'].plot()
    df["MA10"].plot()
    plt.legend(loc=4)
    plt.xlabel("Date")
    plt.ylabel("Price")
    export_pdf.savefig()
    plt.close()
