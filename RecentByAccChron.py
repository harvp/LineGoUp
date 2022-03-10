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
	print("<blockquote class=\"twitter-tweet\"><p>Southern communities inspire change through teaching tech.<br><br>Learn about this digital-first academy: <a href=\"https://t.co/S0TA6FDScf\">https://t.co/S0TA6FDScf</a></p>&mdash; Microsoft (@Microsoft) <a href=\"https://twitter.com/Microsoft/status/1496582638248857600?ref_src=twsrc%5Etfw\">February 23, 2022</a></blockquote>", "<blockquote class=\"twitter-tweet\"><p>Resources to accelerate your inclusion journey: <a href=\"https://t.co/no6T2dNZ7x\">https://t.co/no6T2dNZ7x</a></p>&mdash; Microsoft (@Microsoft) <a href=\"https://twitter.com/Microsoft/status/1496602025718657030?ref_src=twsrc%5Etfw\">February 23, 2022</a></blockquote>")
else:
	print(errorMessage)