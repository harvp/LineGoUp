##Parameter for the user's twitter account name - for Bob Smith @bobsmith123, use "bobsmith123"
##Call should look like TopTweetsByMention.py bobsmith123
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

returnList = [["https://twitter.com/suhemparack/status/1499431019769856000", 5, 3], 
["https://twitter.com/suhemparack/status/1499425824617144321", 2, 0],
["https://twitter.com/suhemparack/status/1499083922038132736", 17, 2],
["https://twitter.com/suhemparack/status/1498390574910500865", 8, 0],
["https://twitter.com/suhemparack/status/1498308588833411074", 1, 0],
["https://twitter.com/suhemparack/status/1498135404540616710", 7, 0]]
errorMessage = ["Error - invalid call", 0, 0]

if len(sys.argv) == 2:
	print(returnList)
else:
	print(errorMessage)