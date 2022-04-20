
import yfinance as yf
import datetime
import pytz
from datetime import date
import sys
import time
import requests
import io


def calc_percent(open_price, close):
    increase = close - open_price
    pct = increase / open_price
    return pct * 100


end = datetime.date.today()
difference = datetime. timedelta(8)
start = end - difference
end = end.strftime("%Y-%m-%d")
start = start.strftime("%Y-%m-%d")

#microsoft is MSFT

symbol = sys.argv[1]
#symbol = "MSFT"

# download the stock price
stockData = []
stockData = yf.download(symbol, start=start, end=end, progress=False)

# append the individual stock prices
if len(symbol) == 0:
    print("Invalid call")
else:
    stockData['Name'] = symbol

tz_utc = pytz.timezone('UTC')
difference = datetime.timedelta(1)
day_1 = datetime.datetime.now(tz_utc)
day_1 = day_1.replace(hour=0, minute=0, second=0, microsecond=0)
day_2 = day_1 - difference
day_3 = day_2 - difference
day_4 = day_3 - difference
day_5 = day_4 - difference
day_6 = day_5 - difference
day_7 = day_6 - difference

stock = stockData.loc[::-1].reset_index().head()

dates = [day_1.strftime("%Y-%m-%d %H:%M:%S"), day_2.strftime("%Y-%m-%d %H:%M:%S"), day_3.strftime("%Y-%m-%d %H:%M:%S"), day_4.strftime("%Y-%m-%d %H:%M:%S"), day_5.strftime("%Y-%m-%d %H:%M:%S"), day_6.strftime("%Y-%m-%d %H:%M:%S"), day_7.strftime("%Y-%m-%d %H:%M:%S")]

priceData = []
i = 0
volume = 0
open_val = 0
close = 0
tx_count = 0
average_pct = 0
average_volume = 0
percent_change = 0
for date in dates:
    flag = False
    for stock_date in stock["Date"]:
        if str(stock_date) == date:
            volume = stock["Volume"][i]
            percent_change = calc_percent(stock["Open"][i], stock["Close"][i])
            average_volume += volume
            open_val = stock["Open"][i]
            close = stock["Close"][i]
            priceData.append([date, volume, open_val, close, percent_change])
            flag = True
            i += 1
            tx_count += 1
    if not flag:
        priceData.append([date, 0, open_val, close, 0])

average_volume = average_volume / tx_count
average_pct = 0
priceData.append([date, volume, open_val, close])
outputString = "<h2> Stock Report for " + symbol + "</h2><table>"
outputString += "<tr><th>Date</th><th>Trade Volume</th><th>Opening Price</th><th>Closing Price</th></tr>"
i = 0
for record in priceData:
    outputString += "<tr><td>" + str(dates[i]) + "</td>"
    outputString += "<td>" + str(record[1]) + "</td>"
    outputString += "<td>" + str(record[2]) + "</td>"
    outputString += "<td>" + str(record[3]) + "</td></tr>"
    average_pct += record[4]
    i += 1
    if i == 7:
        break

outputString += "<tr><td>---------------</td></tr>"
outputString += "<tr><td>Average Volume Per Trading Day: </td><td></td><td>" + str(average_volume) + "</td></tr>"
average_pct = average_pct / tx_count
outputString += "<tr><td>Average % Change in Price Per Day: </td><td></td><td>" + str(average_pct) + "</td></tr></table>"
print(outputString)