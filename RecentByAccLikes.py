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


errorMessage = ["Error - invalid call", 0, 0]

if len(sys.argv) == 2:
	print("https://twitter.com/Microsoft/status/1496602021323022338?ref_src=twsrc%5Etfw")
else:
	print(errorMessage)