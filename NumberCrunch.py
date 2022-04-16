import pytz
import math
import yfinance as yf
import datetime
import sys
import tweepy


def calc_percent(open_price, close):
    increase = close - open_price
    pct = increase / open_price
    return pct * 100


def calc_daily_vi(individual, average, twit_daily, twit_average):

    x = individual - average
    y = twit_daily - twit_average
    numerator = x * y
    denominator = math.sqrt((x * x) * (y * y))
    return abs(numerator/denominator)


errorMessage = "Error - invalid call"
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAHn2ZAEAAAAARCtdfQEvwI7L53ZL2oVUn0OW%2FEY%3DOB3SQ9Q9C8W5B8SRvXvrXRi5ztUm3TtDTQePdvlUew3x6efS2a")

# if len(sys.argv) != 3:
#    print(errorMessage)
#
# user = sys.argv[1]
# ticker = sys.argv[2]

user = "microsoft"
t_user = client.get_user(username="microsoft")
id_num = t_user[0]["id"]
query = 'from:' + user + " -is:retweet"
response = client.search_recent_tweets(query=query,
                                       tweet_fields=['context_annotations', 'created_at', 'public_metrics'],
                                       max_results=10)

tz_utc = pytz.timezone('UTC')
difference = datetime.timedelta(1)
day_1 = datetime.datetime.now(tz_utc)
day_2 = day_1 - difference
day_3 = day_2 - difference
day_4 = day_3 - difference
day_5 = day_4 - difference
day_6 = day_5 - difference
day_7 = day_6 - difference

engagement_scores = [0, 0, 0, 0, 0, 0, 0]
tweets_per_day = [0, 0, 0, 0, 0, 0, 0]

cumulative_engagement = 0
cumulative_count = 0
for tweet in response[0]:
    if tweet["created_at"] > day_2:  # day 1
        engagement_scores[0] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[0] += 1
    elif tweet["created_at"] > day_3:  # day 2
        engagement_scores[1] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[1] += 1
    elif tweet["created_at"] > day_4:  # day 3
        engagement_scores[2] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[2] += 1
    elif tweet["created_at"] > day_5:  # day 4
        engagement_scores[3] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[3] += 1
    elif tweet["created_at"] > day_6:  # day 5
        engagement_scores[4] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[4] += 1
    elif tweet["created_at"] > day_7:  # day 6
        engagement_scores[5] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[5] += 1
    else:  # day 7
        engagement_scores[6] += (tweet["public_metrics"]["retweet_count"] * 2) + (tweet["public_metrics"]["like_count"]) + (tweet["public_metrics"]["quote_count"] * 3)
        tweets_per_day[6] += 1

for value in engagement_scores:
    cumulative_engagement += value

for day in tweets_per_day:
    cumulative_count += day

average_engagement = cumulative_engagement / cumulative_count

end = datetime.date.today()
difference = datetime.timedelta(8)
start = end - difference
end = end.strftime("%Y-%m-%d")
start = start.strftime("%Y-%m-%d")

#microsoft is MSFT
#symbol = sys.argv[1]
ticker = "MSFT"

# download the stock price
stockData = []
stockData = yf.download(ticker, start=start, end=end, progress=False)

stock = stockData.reset_index()


dates = []
for index in range(0, 9):
    difference = datetime.timedelta(index)
    dateEntry = (datetime.datetime.now()- difference)
    appendation = dateEntry.strftime("%Y-%m-%d") + ' 00:00:00'
    dates.append(appendation)

dates.sort()
priceData = []
i = 0
volume = 0
open_val = 0
close = 0
tx_count = 0
average_pct = 0
average_volume = 0
for date in dates:
    flag = False
    for stock_date in stock["Date"]:
        if str(stock_date) == date:
            percent_change = calc_percent(stock["Open"][i], stock["Close"][i])
            volume = stock["Volume"][i]
            average_volume += volume
            open_val = stock["Open"][i]
            close = stock["Close"][i]
            average_pct += percent_change
            priceData.append([date, percent_change, volume, open_val, close, 0.0, 0.0])
            flag = True
            i += 1
            tx_count += 1
    if not flag:
        priceData.append([date, 0.0, 0, open_val, close, 0.0, 0.0])

average_pct = average_pct / tx_count
average_volume = volume / tx_count

i = 0
priceData.sort(reverse=True)
for record in priceData:
    if record[2] != 0:
        record[5] = calc_daily_vi(record[1], average_pct, engagement_scores[i], average_engagement)
        record[6] = calc_daily_vi(record[2], average_volume, engagement_scores[i], average_engagement)
        i += 1

print(priceData)


