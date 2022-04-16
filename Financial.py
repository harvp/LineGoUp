
import yfinance as yf
import datetime
import sys
from datetime import date
import time
import requests
import io

end = datetime.date.today()
difference = datetime. timedelta(8)
start = end - difference
end = end.strftime("%Y-%m-%d")
start = start.strftime("%Y-%m-%d")

#microsoft is MSFT

#symbol = sys.argv[1]
symbol = "MSFT"

# download the stock price
stock = []
stock = yf.download(symbol, start=start, end=end, progress=False)


# append the individual stock prices
if len(stock) == 0:
    print("Invalid call")
else:
    stock['Name'] = symbol

print(stock)