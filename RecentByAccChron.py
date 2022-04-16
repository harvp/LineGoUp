##Parameter for the user's twitter account name - for Bob Smith @bobsmith123, use "bobsmith123"
##Call should look like RecentByAccChron.py bobsmith123
##Returns a list of URLs for the most recent tweets by that user, ordered most recent to least. Right now the tweets are from the past 7 days

#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import sys
import getopt
import tweepy
import re
import sys


errorMessage = "Error - invalid call"

if len(sys.argv) != 2:
    print(errorMessage)

#print("<blockquote class=\"twitter-tweet\"><p>Southern communities inspire change through teaching tech.<br><br>Learn about this digital-first academy: <a href=\"https://t.co/S0TA6FDScf\">https://t.co/S0TA6FDScf</a></p>&mdash; Microsoft (@Microsoft) <a href=\"https://twitter.com/Microsoft/status/1496582638248857600?ref_src=twsrc%5Etfw\">February 23, 2022</a></blockquote>", "<blockquote class=\"twitter-tweet\"><p>Resources to accelerate your inclusion journey: <a href=\"https://t.co/no6T2dNZ7x\">https://t.co/no6T2dNZ7x</a></p>&mdash; Microsoft (@Microsoft) <a href=\"https://twitter.com/Microsoft/status/1496602025718657030?ref_src=twsrc%5Etfw\">February 23, 2022</a></blockquote>")
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHn2ZAEAAAAARCtdfQEvwI7L53ZL2oVUn0OW%2FEY%3DOB3SQ9Q9C8W5B8SRvXvrXRi5ztUm3TtDTQePdvlUew3x6efS2a")

user = sys.argv[1]
query = 'from:' + user + " -is:retweet"
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'public_metrics'], max_results=100)
counter = 0

for tweet in tweets.data:
    counter += 2

#print(counter)
outputString = "\'"
for tweet in tweets.data:
    tweetURL = "https://twitter.com/" + user + "/status/" + str(tweet.id)
    outputString += "<blockquote class=\"twitter-tweet\"><p>" + "<a href=\"" + tweetURL + "\"></a></p></blockquote>"
    #print(tweet.text)
    #print(tweetURL)

outputString += "\'"

print(outputString)
