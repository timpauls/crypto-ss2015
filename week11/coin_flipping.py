#!/usr/bin/env python2
"""Coin flipping (see Schneier, Applied Cryptography, Chapter 4.10)"""

import hashlib
import Crypto.Random.random

HEADS = 0
TAILS = 1

EVEN = 0
ODD = 1

# In a clean implementation, we would model Alice and Bob as objects.
# Since we do not want to dig into the object oriented features of
# Python, you will have to use global variables.  In order to use a
# global variable "foo" instead of the local one, declare it in the
# function as
#
# global foo
#

##########################################
#
# Alice
#
##########################################

#
# In this impelementation, Alice may try to cheat.
#

def alice(cheat):
    x = Crypto.Random.random.randint(0,2**128)
    y = hashlib.sha256(repr(x))
    bobsAnswerToChallenge = bobProcessessChallenge(y)
    if(cheat):
        # Alice decides to cheat:
        # If x was an even number, she
        # replaces it with an odd number
        # and vice versa.
        xOld = x
        while(True):
            x = Crypto.Random.random.randint(0,2**128)
            if((xOld+x) % 2 == 1):
                break
    bobGetsAlicesSecret(x)
    if((x % 2) == bobsAnswerToChallenge):
        coinAccordingToAlice = HEADS
    else:
        coinAccordingToAlice = TAILS
    return(coinAccordingToAlice)

##########################################
#
# Bob
#
##########################################

# Your task is to implement Bob's role in the protocol. For this, two
# functions have to be implemented. Variables that you want to share
# between the functions must be declared as global.  Bob's conclusion,
# i.e. his opinion about the result of the coin flip, shall be stored
# in global variable coinAccordingToBob. If Bob discovers a cheating
# attempt, global variable coinAccordingToBob shall be set to None.

coinAccordingToBob = None
yBobReceived = 0
bobsGuess = 0

def bobProcessessChallenge(y):
    global yBobReceived
    global bobsGuess

    yBobReceived = y
    bobsGuess = Crypto.Random.random.randint(EVEN, ODD)
    return bobsGuess

def bobGetsAlicesSecret(x):
    global yBobReceived
    global coinAccordingToBob
    global bobsGuess

    y = hashlib.sha256(repr(x))
    if yBobReceived.digest() == y.digest():
        if (x % 2) == bobsGuess:
            coinAccordingToBob = HEADS
        else:
            coinAccordingToBob = TAILS
    else:
        coinAccordingToBob = None

def test():
    for _ in xrange(0x100):
        coinAccordingToAlice = alice(cheat=False)
        assert(coinAccordingToAlice == coinAccordingToBob)
    for _ in xrange(0x100):
        coinAccordingToAlice = alice(cheat=True)
        assert(coinAccordingToBob == None)

if __name__ == "__main__":
    test()
