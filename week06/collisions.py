#!/usr/bin/env python2
#
# In this exercise, you will mount a pre-image and a collision attack
# on SHA-256. Since SHA-256 is not broken, you will mount the attack
# on the first bytes of the hash only.

import random
import Crypto.Hash.SHA256
import pdb
import itertools
import string
import datetime
import os

DEBUG = False

blockSize = 64 # 64 * 8 = 512 bit

def prettyPrintHexList(l):
    numbersPerLine = 16
    i = 0
    s = ''
    for c in l:
        s += '%02X' % ord(c)
        i += 1
        if(i == numbersPerLine):
            s += '\n'
            i = 0
        else:
            s += ' '
    if((len(l) % numbersPerLine) != 0):
       s += '\n'
    return(s)
    
# In this exercise, we only use the first three bytes of SHA-256 hashs,
# i.e. when calculating a hash, we cut it after the third byte.
#
# Your goal is to mount a pre-image attack on the hash
#
# FF FF FF
#
# I.e. find a byte sequence (message) with a SHA-256 hash starting with
# FF FF FF.

def preimage(digest):
    """Find preimage for digest.

    Function test() shows how this function is called."""

    log("Starting preimage...")

    for length in xrange(10):
        for s in itertools.imap(''.join, itertools.product(string.ascii_letters + string.digits + string.punctuation + string.whitespace, repeat=length)):
            sha = Crypto.Hash.SHA256.new()
            sha.update(s)
            mydigest = sha.digest()
            dig = mydigest[:3]
            if dig == digest:
                log("Found preimage!")
                log("Message: %s; Digest: %s"%(s, mydigest))
                return (s, mydigest)

    return(None, None)

# In this exercise, we only use the first five bytes of SHA-256 hashs,
# i.e. when calculating a hash, we cut it after the fifth byte.
# 
# Your goal is to mount a collision attack, i.e. find two byte
# sequences (messages) for which the first five bytes of the SHA-256
# hash are identical.
def collision(digestLength):
    """Find collision for digest.

    Function test() shows how this function is called."""

    log("Starting collision test...")

    hashedWords = {}
    length = 32

    while True:
        randomString = os.urandom(length)
        sha = Crypto.Hash.SHA256.new()
        sha.update(randomString)
        digest = sha.digest()
        dig = digest[:digestLength]

        log("%s - %s"%(prettyPrintHexList(list(randomString)), prettyPrintHexList(list(digest))))

        if dig not in hashedWords:
            hashedWords[dig] = (randomString, digest)
            log("Inserted. New size: %d"%(len(hashedWords)))
        else:
            log("Found match!")
            log("%s - %s"%(randomString, digest))
            log("%s - %s"%(hashedWords[dig][0], hashedWords[dig][1]))
            return (randomString, digest, hashedWords[dig][0], hashedWords[dig][1])

    return(None, None, None, None)

def log(string):
    if DEBUG:
        print "[%s] %s"%(datetime.datetime.now(), string)

def test():
    print('********')
    print('Preimage')
    print('********\n')
    (msg, digest) = preimage('\xFF\xFF\xFF')
    print('Message:')
    print(prettyPrintHexList(list(msg)))
    print('Digest:')
    print(prettyPrintHexList(list(digest)))

    print('*********')
    print('Collision')
    print('*********\n')
    (m0, d0, m1, d1) = collision(5)
    print('First Message:')
    print(prettyPrintHexList(list(m0)))
    print('Digest:')
    print(prettyPrintHexList(list(d0)))
    print('Second Message:')
    print(prettyPrintHexList(list(m1)))
    print('Digest:')
    print(prettyPrintHexList(list(d1)))

test()