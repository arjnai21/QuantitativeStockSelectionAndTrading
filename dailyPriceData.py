from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime
# token="sk_957a78ce716949109cf36f83b9cc3fd2"

start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)

apple = Stock("AAPL", token="sk_957a78ce716949109cf36f83b9cc3fd2")
print(apple.get_price())



