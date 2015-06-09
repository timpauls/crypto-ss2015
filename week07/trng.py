#!/usr/bin/env python

"""True Random Number Generator"""

# Write a true random number generator. In order to do so, you have to
# identify a source of true randomness. Creative sources of randomness
# are appreciated. If you cannot use Python/Sage for this assignment,
# e.g. because you want to access low-level functionality not
# available in Python/Sage, you may also submit C code for this
# assignment.
#
# Your function shall output 20000 random bits as byte values,
# i.e. it should write a file of 2500 random bytes.

import urllib2
import xml.etree.ElementTree as ET
from datetime import datetime

FILENAME='random.dat'
N=2500

# Using heise.de newsfeed as entropy source.
# This RNG fetches the heise.de newsfeed, selects a headline based on the current time (seconds),
# selects a character from that headline based on the current time (microseconds) and appends
# that character to the result.
# Since every byte triggers a new network call, added randomness is generated from the time
# that call takes to complete.
# Also, this is slow as fuck.
def trng_heise_news(bytes):
	URL = "http://heise.de.feedsportal.com/c/35207/f/653902/index.rss"
	result = []
	for n in xrange(bytes):
		# load newsfeed
		urlContent = urllib2.urlopen(URL).read()
		root = ET.fromstring(urlContent)

		# create list of all headlines
		headlines = []
		for item in root.iter('item'):
			headlines.append(item.find('title').text)

		now = datetime.now()

		# map current second to headline in list
		headline = headlines[int(len(headlines) / 60.0 * now.second)]

		# map current microsecond to character in headline
		char = headline[int(len(headline) / 1000000.0 * now.microsecond)]
		result.append(char)
		import sys
		sys.stdout.write("Progress: %2.2f%%\r"%(100.0*n/bytes))
		sys.stdout.flush()

	return result



def trng(filename, n):
    rn = []

    rn = trng_heise_news(n)

    rnFile = open(filename, 'wb')
    for i in rn:
        rnFile.write(i)
    rnFile.close()

if __name__ == "__main__":
    trng(filename=FILENAME, n=N)
