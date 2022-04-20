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
    denominator = math.sqrt((average * average) * (twit_average * twit_average))
    return numerator/denominator


errorMessage = "Error - invalid call"
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAHn2ZAEAAAAARCtdfQEvwI7L53ZL2oVUn0OW%2FEY%3DOB3SQ9Q9C8W5B8SRvXvrXRi5ztUm3TtDTQePdvlUew3x6efS2a")

if len(sys.argv) != 3:
    print(errorMessage)

user = sys.argv[1]
ticker = sys.argv[2]

#user = "microsoft"
t_user = client.get_user(username=user)
id_num = t_user[0]["id"]
company_name = t_user.data.name
query = 'from:' + user + " -is:retweet"
response = client.search_recent_tweets(query=query,
                                       tweet_fields=['context_annotations', 'created_at', 'public_metrics'],
                                       max_results=100)

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
#ticker = "MSFT"

# download the stock price
stockData = []
stockData = yf.download(ticker, start=start, end=end, progress=False)


#stock = stockData.loc[::-1].reset_index().head()

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

correlation = 0
numerator_pct_sum = 0
numerator_volume_sum = 0
denominator_pct_sum = 0
denominator_volume_sum = 0
denominator_engagement_sum = 0
i = 0
for record in priceData:
    numerator_pct_sum += ((record[1] - average_pct) * (engagement_scores[i] - average_engagement))
    numerator_volume_sum += ((record[2] - average_volume) * (engagement_scores[i] - average_engagement))
    denominator_pct_sum += (record[1] - average_pct) * (record[1] - average_pct)
    denominator_volume_sum += (record[2] - average_volume) * (record[2] - average_volume)
    denominator_engagement_sum += (engagement_scores[i] - average_engagement) * (
                engagement_scores[i] - average_engagement)
    i += 1
    if i == 7:
        break

pct_vi = numerator_pct_sum / (math.sqrt(denominator_pct_sum * denominator_engagement_sum))
volume_vi = numerator_volume_sum / (math.sqrt(denominator_volume_sum * denominator_engagement_sum))
# print("The VI for the change in price is " + str(pct_vi))
# print("The VI for the change in volume is " + str(volume_vi))

outputString = "<h2> Volatility Report for " + company_name + "</h2><table cellpadding=5>"
outputString += "<center><tr><th>Date</th><th>Price Change</th><th>Trade Volume</th><th>Twitter Engagement Score</th></tr>"
i = 0
for record in priceData:
    outputString += "<tr><td>" + str(dates[i]) + "</td>"
    outputString += "<td>" + str(record[1]) + "</td>"
    outputString += "<td>" + str(record[2]) + "</td>"
    outputString += "<td>" + str(engagement_scores[i]) + "</td></tr>"
    i += 1
    if i == 7:
        break

outputString += "<tr><td>---------------</td></tr>"
outputString += "<tr><td>Volatility Index by Trades: </td><td></td><td>" + str(volume_vi) + "</td></tr>"
outputString += "<tr><td>Volatility Index by Price Change: </td><td></td><td>" + str(pct_vi) + "</td></tr></center></table>"

print(outputString)