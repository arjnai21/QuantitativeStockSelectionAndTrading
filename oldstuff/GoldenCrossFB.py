import quandl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np

# Lines 19-41 adapted from
# https://www.jasonlee.mobi/projects/2018/5/18/building-a-momentum-trading-strategy-using-python

ticker = "FB"
df = quandl.get('WIKI/' + ticker, api_key="T2K2v57vDVL9Wwx_ia3c")
df["MA5"] = df['Close'].rolling(5).mean()
df["MA20"] = df['Close'].rolling(20).mean()

signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['MA5'] = df["MA5"]
signals["MA20"] = df["MA20"]
signals['signal'][5:] = np.where(signals["MA5"][5:]
                                 > signals['MA20'][5:], 1.0, 0.0)

signals['positions'] = signals['signal'].diff()
signals['positions'] = signals['positions'].shift(periods=1)
fig = plt.figure(figsize=(20, 15))

ax1 = fig.add_subplot(111, ylabel="Price")

df['Close'].plot(ax=ax1)
df['MA5'].plot(ax=ax1)
df["MA20"].plot(ax=ax1)


ax1.plot(signals.loc[signals.positions == 1.0].index,
         df.Close[signals.positions == 1.0],
         marker='o', markersize=10, color='y',
         linestyle="None")

ax1.plot(signals.loc[signals.positions == -1.0].index,
         df.Close[signals.positions == -1.0],
         marker='o', markersize=10, color='y',
         linestyle="None", markerfacecolor="None")

startInd = -1

for i in range(len(signals['positions'])):
    if signals['positions'][i] == 1:
        startInd = i

    if signals['positions'][i] == -1 and startInd != -1:
        ax1.plot(df["Close"][startInd:i], color='black')
        startInd = -1


plt.legend(loc="best")
plt.xlabel("Date")
plt.ylabel("Price")
with PdfPages(r'C:\Users\arjun\PycharmProjects\QuantitativeStockSelectionAndTrading\FBGoldenCross.pdf') as export_pdf:
    export_pdf.savefig()
    plt.close()
