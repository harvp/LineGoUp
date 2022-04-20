import os
import pandas as pd
import tweepy
import json

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHn2ZAEAAAAARCtdfQEvwI7L53ZL2oVUn0OW%2FEY%3DOB3SQ9Q9C8W5B8SRvXvrXRi5ztUm3TtDTQePdvlUew3x6efS2a")


# Replace with your own search query
user = "suhemparack"
query = 'from:' + user + " -is:retweet"

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    #print(tweet.text)
    tweetURL = "https://twitter.com/" + user + "/status/" + str(tweet.id)
    outputString = "<blockquote class=\"twitter-tweet\"><p>" + tweet.text + "<a href=\"" + tweetURL + "\"></a></p></blockquote>"
    print(outputString)


