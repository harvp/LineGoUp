##Parameter for the user's twitter account name - for Bob Smith @bobsmith123, use "bobsmith123"
##Call should look like RecentByAccLikes.py bobsmith123
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

errorMessage = "Error - invalid call"

if len(sys.argv) != 2:
    print(errorMessage)

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHn2ZAEAAAAARCtdfQEvwI7L53ZL2oVUn0OW%2FEY%3DOB3SQ9Q9C8W5B8SRvXvrXRi5ztUm3TtDTQePdvlUew3x6efS2a")

user = sys.argv[1]
query = 'from:' + user + " -is:like"
tweets = client.get_liking_users(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
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
