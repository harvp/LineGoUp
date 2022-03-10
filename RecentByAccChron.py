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


errorMessage = "Error - invalid call"

if len(sys.argv) == 2:
	print("https://twitter.com/suhemparack/status/1499431019769856000","https://twitter.com/suhemparack/status/1499425824617144321", "https://twitter.com/suhemparack/status/1499083922038132736", "https://twitter.com/suhemparack/status/1498390574910500865", "https://twitter.com/suhemparack/status/1498308588833411074", "https://twitter.com/suhemparack/status/1498135404540616710")
else:
	print(errorMessage)