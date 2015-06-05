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
            dig = sha.digest()[:3]
            if dig == digest:
                log("Found preimage!")
                log("Message: %s; Digest: %s"%(s, digest))
                return (s, digest)

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

    for length in xrange(3, 10):
        for s1 in itertools.imap(''.join, itertools.product(string.ascii_letters + string.digits + string.punctuation + string.whitespace, repeat=length)):
            log("Testing left block %s"%(s1))

            for s2 in itertools.imap(''.join, itertools.product(string.ascii_letters + string.digits + string.punctuation + string.whitespace, repeat=length)):
                if s1 != s2:
                    sha = Crypto.Hash.SHA256.new()
                    sha.update(s1)
                    digest1 = sha.digest()
                    dig1 = digest1[:digestLength]

                    sha = Crypto.Hash.SHA256.new()
                    sha.update(s2)
                    digest2 = sha.digest()
                    dig2 = digest2[:digestLength]

                    if dig1 == dig2:
                        log("Found collision!!")
                        log("S1: %s; Digest1: %s"%(s1, digest1))
                        log("S2: %s; Digest2: %s"%(s2, digest2))
                        return (s1, digest1, s2, digest2)

    return(None, None, None, None)

def log(string):
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