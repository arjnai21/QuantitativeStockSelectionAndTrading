import quandl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


ticker = "FB"
df = quandl.get('WIKI/' + ticker, api_key="insert api key")
df["MA5"] = df['Close'].rolling(5).mean()
df["MA10"] = df['Close'].rolling(10).mean()


with PdfPages(r'insert file path') as export_pdf:
    df['Close'].plot()
    df['MA5'].plot()
    df["MA10"].plot()
    plt.legend(loc=4)
    plt.xlabel("Date")
    plt.ylabel("Price")
    export_pdf.savefig()
    plt.close()
