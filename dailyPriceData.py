from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime
import csv

import matplotlib.pyplot as plt
# token="sk_957a78ce716949109cf36f83b9cc3fd2"

start = datetime(2019, 1, 1)
end = datetime(2019, 6, 23)


with open("aapl_test.csv", mode="w") as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    apple = get_historical_data("AAPL", start, end, token="sk_957a78ce716949109cf36f83b9cc3fd2", output_format = 'pandas')
    apple.to_csv(path_or_buf=file)



