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
response = client.get_users_mentions( id=id_num, tweet_fields=['context_annotations', 'created_at', 'public_metrics'], max_results=100)

print(response)
for tweet in response:
    print(tweet)
