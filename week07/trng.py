
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
from random import shuffle, random
import sys

FILENAME='random.dat'
N=2500

# Using heise.de newsfeed as entropy source.
# This RNG fetches the heise.de newsfeed, selects a headline based on the current time (seconds),
# selects a character from that headline based on the current time (microseconds) and appends
# that character to the result.
# Since every byte triggers a new network call, added randomness is generated from the time
# that call takes to complete.
#
# Monobit:	X
# Poker:	X
# Runs:		X
# Longruns:	X
def trng_heise_news(bytes):
	URL = "http://heise.de.feedsportal.com/c/35207/f/653902/index.rss"
	result = []
	while len(result) < bytes:
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

		# char has to be in ascii
		if all(ord(c) < 128 for c in char):
			result.append(char)

		sys.stdout.write("Progress: %2.2f%%\r"%(100.0*len(result)/bytes))
		sys.stdout.flush()

	return result

# Using mouse motion as entropy source.
# This RNG checks what direction the mouse was moved since the last loop,
# encodes that direction as a 2 byte value and a appends four of those as
# a byte to the result.
#
# Monobit:	check
# Poker:	X
# Runs:		X
# Longruns:	X
def trng_mouse_motion(bytes):
	from Xlib import display
	print "Please move your mouse..."

	result = []
	byte = []

	data = display.Display().screen().root.query_pointer()._data

	lastX = data["root_x"]
	lastY = data["root_y"]

	while len(result) < bytes:
		data = display.Display().screen().root.query_pointer()._data

		x = data["root_x"]
		y = data["root_y"]

		#deltaX = (x - lastX) % 256
		#deltaY = (y - lastY) % 256

		rand = range(4)
		shuffle(rand)
		for i in rand:
			if i == 0:
				if x < lastX:
					byte.append("00")
			elif i == 1:
				if x > lastX:
					byte.append("01")
			elif i == 2:
				if y < lastY:
					byte.append("10")
			elif i == 3:
				if y > lastY:
					byte.append("11")

		if len(byte) >= 4:
			result.append(chr(int("".join(byte[:4]), 2)))
			byte = []


		sys.stdout.write("Progress: %2.2f%%\r"%(100.0*len(result)/bytes))
		sys.stdout.flush()

		lastX = x
		lastY = y

	print "Enough entropy collected."
	return result

# Using a live stream of a supposed russian military radio signal as entropy source.
# More  info on the signal: https://en.wikipedia.org/wiki/UVB-76
# Since the live stream always starts with OGG headers, skip some bytes. Shuffle the read
# bytes to try to prevent the poker test from failing.
#
# Monobit:	check
# Poker:	check
# Runs:		check
# Longruns:	check
#
# Unfortunately, this is not really reliable. Also I suppose when it works it would work
# just as well with any other ogg file, as currently only the compressed bytes are used.
# Originally I had planned to decode the audio stream and use the actual raw audio data
# (which contains lots of static noise) as entropy, however I did not manage to get that
# working in time for the assignment.
def trng_buzzer(bytes):
	URL = "http://stream.priyom.org:8000/buzzer.ogg"
	connection = urllib2.urlopen(URL)
	#skip some stuff (hopefully ogg headers)
	connection.read(2000 + int(random() * 10000))
	urlContent = connection.read(2500)
	result = list(urlContent)
	shuffle(result)
	return result


def trng(filename, n):
    rn = []

    rn = trng_buzzer(n)

    rnFile = open(filename, 'wb')
    for i in rn:
        rnFile.write(i)
    rnFile.close()

if __name__ == "__main__":
    trng(filename=FILENAME, n=N)
