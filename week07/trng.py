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

URL = "http://heise.de.feedsportal.com/c/35207/f/653902/index.rss"

def trng_test(bytes):
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
		print char
		result.append(char)
		print "".join(result)

	print "".join(result)



def trng(filename, n):
    rn = []
##################
# YOUR CODE HERE #
##################
    rnFile = open(filename, 'wb')
    for i in rn:
        rnFile.write(i)
    rnFile.close()

if __name__ == "__main__":
	trng_test(32)
    #trng(filename=FILENAME, n=N)
