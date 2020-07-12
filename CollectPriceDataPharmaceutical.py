from yahoofinancials import YahooFinancials
import csv
import datetime
import os


def collectData():
    start_date = "1792-05-17"
    end_date = datetime.date.today().__str__()

    if not os.path.exists('pharmaceutical_data_new'):
        os.mkdir('pharmaceutical_data_new')
    print("made directory")
    file = list(open("FDA_data20182019.csv"))
    print(type(file))
    for i in range(1, len(file)):
        print(type(file))
        line_arr = file[i].strip("\n").split(",")
        # if line_arr[1] == "NODATE" or line_arr[2] == "NODATA"or line_arr[2] == "OUTCOME":
        #     continue
        ticker = line_arr[0]
        drug_name = line_arr[1]
        drug_name = drug_name.replace("/", "-")
        print(ticker)
        end_date = datetime.datetime.strptime(line_arr[2], "%m/%d/%Y").strftime("%Y-%m-%d")
        if os.path.exists('pharmaceutical_data_new/' + ticker + "_" + drug_name + "_" + end_date + '.csv'):
            continue
        # collect historical data for ticker
        financials = YahooFinancials(ticker)
        data = financials.get_historical_price_data(start_date, end_date, "daily")
        if data[ticker] is None or "prices" not in data[ticker].keys():
            continue
        prices = data[ticker]["prices"][-91:]

        # header of csv
        ordering = ['distance','date' , 'open', 'close', 'high', 'low', 'volume']
        counter = -90

        # rearrange values with different keys
        for j in range(len(prices)):
            formatted_dict = {}
            for k in ordering:
                if k == 'distance':
                    formatted_dict[k] = counter
                elif k == 'date':
                    formatted_dict[k] = prices[j]['formatted_date']
                else:
                    formatted_dict[k] = prices[j][k]
            prices[j] = formatted_dict
            counter += 1

        keys = prices[0].keys()

        # write prices dictionary to csv file
        with open('pharmaceutical_data_new/' + ticker + "_" + drug_name + "_" + end_date + '.csv', 'w',
                  newline='') as write_file:
            dict_writer = csv.DictWriter(write_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(prices)

collectData()