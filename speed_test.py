from yahoofinancials import YahooFinancials
import time

ZAZZTFinancials = YahooFinancials("ZAZZT")
AAPLFinancials = YahooFinancials("AAPL")

start_time = time.time()
zazzt_price = ZAZZTFinancials.get_current_price()
elapsed = time.time() - start_time
print("ZAZZT Price: " + zazzt_price.__str__() + "\nTime Taken: " + str(elapsed))
print()
start_time = time.time()
aapl_price = AAPLFinancials.get_current_price()
elapsed = time.time() - start_time
print("AAPL Price: " + aapl_price.__str__() + "\nTime Taken: " + str(elapsed))
print()
start_time = time.time()
zazzt_avg = ZAZZTFinancials.get_yearly_low()
elapsed = time.time() - start_time
print("ZAZZT 50_day_moving_avg: " + zazzt_avg.__str__() + "\nTime Taken: " + str(elapsed))
print()
start_time = time.time()
aapl_avg = AAPLFinancials.get_yearly_low()
elapsed = time.time() - start_time
print("AAPL 50_day_moving_avg: " + aapl_avg.__str__() + "\nTime Taken: " + str(elapsed))