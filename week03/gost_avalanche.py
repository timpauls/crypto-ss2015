#!/usr/bin/env python2

DEBUG=0

# We are going to use the following keys and plaintexts in this
# assignment.
plaintext0 = 0x02468ACEECA86420
plaintext1 = 0x12468ACEECA86420
key0       = 0x08C73A08514436F2E150A865EB75443F904396E66638E182170C1CA1CB6C1062
key1       = 0x18C73A08514436F2E150A865EB75443F904396E66638E182170C1CA1CB6C1062

# We use the s-boxes of Central Bank of Russian Federation in this
# assignment.
sboxes = [ [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
           [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
           [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
           [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
           [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
           [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
           [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
           [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12] ]

# This week's assignment is to meausure the avalance effect in GOST,
# both for changes in the plaintext and in the key. As you can see,
# the two plaintexts and the two keys differ in 1 bit, respectively.
#
# In order to measure the avalance effect for differences in the
# plaintext, you encrypt both plaintext0 and plaintext1 with
# key0. After each round of encryption, you measure how many bits of
# the intermediate ciphertexts differ.
#
# In order to measure the avalance effect for difference in the key,
# you encrypt plaintext0 both with key0 and with key1. Again, you
# measure how many bits of the intermediate ciphertexts differ.
#
# In order to complete this assignment, you have to write your own
# implementation of GOST. You can use function testEncrypt() to check
# if your implementation is correct. Even if your implementation does
# not encrypt to the same ciphertext as in the example, please carry
# on and measure the avalance effects for your implementation.


def gostEncrypt(plaintext, key, rounds=32):
    left = (plaintext & (0xFFFFFFFF << 32)) >> 32
    right = plaintext & 0xFFFFFFFF

    ciphertext = performGost(left, right, key, 1, rounds)

    return(ciphertext)

# You will probably need a number of utility functions to implement
# gostEncrypt.

def getGostRoundKey(key, round, maxRounds):
    if round <= maxRounds - 8:
        return (key & (0xFFFFFFFF << ((round-1)%8)*32)) >> (((round-1)%8)*32)
    else:
        return getGostRoundKey(key, maxRounds-round + 1, maxRounds)

def get4bitChunk(input, chunkNo):
    return (input & (0xF << (chunkNo)*4)) >> (chunkNo) * 4

def applySBoxes(input):
    result = 0x0
    for i in range(8):
        chunk = get4bitChunk(input, i)
        sboxed = sboxes[i][chunk]
        result += sboxed << i*4
    return result

def rotateBy11Bits(input):
    firstElevenBits = input & 0xFFE00000
    last21Bits = input & 0x1FFFFF
    return (last21Bits << 11) + (firstElevenBits >> 21)

def gostRoundFunction(input, key, round, maxRounds):
    subkey = getGostRoundKey(key, round, maxRounds)
    print "Round Key: " + hex(subkey)
    output = (input + subkey) % 0x100000000
    print "R + Round Key: " + hex(output)
    output = applySBoxes(output)
    print "s-Box Application: " + hex(output)
    output = rotateBy11Bits(output)
    print "Shift Left: " + hex(output)
    return output

def performGost(left, right, key, round, maxRounds):
    print "Round: %d"%round
    print "Left: %s"%hex(left)
    print "Right: %s"%hex(right)

    newLeft = right
    newRight = left ^ gostRoundFunction(right, key, round, maxRounds)
    if round < maxRounds:
        return performGost(newLeft, newRight, key, round+1, maxRounds)
    else:
        return (newLeft << 32) + newRight

def bitDifference(a, b):
    """Return number of bits different between a and b."""
    pass
##################
# YOUR CODE HERE #
##################

def testEncrypt():
    assert(gostEncrypt(plaintext=plaintext0, key=key0) ==
           0x8470BE35A752F0CB)
    # Since it is notoriously hard to get bit ordering in crypto
    # algorithms right, here are the temporary values for the first
    # four rounds of encryption:
    #
    # Round:             1
    # Left:              0x02468ACE
    # Right:             0xECA86420
    # Round Key:         0xCB6C1062
    # R + Round Key:     0xB8147482
    # S-Box Application: 0xE0B5FA29
    # Shift Left:        0xAFD14F05
    # Round:             2
    # Left:              0xECA86420
    # Right:             0xAD97C5CB
    # Round Key:         0x170C1CA1
    # R + Round Key:     0xC4A3E26C
    # S-Box Application: 0x638151F7
    # Shift Left:        0x0A8FBB1C
    # Round:             3
    # Left:              0xAD97C5CB
    # Right:             0xE627DF3C
    # Round Key:         0x6638E182
    # R + Round Key:     0x4C60C0BE
    # S-Box Application: 0x5616B515
    # Shift Left:        0xB5A8AAB0
    # Round:             4
    # Left:              0xE627DF3C
    # Right:             0x183F6F7B
    # Round Key:         0x904396E6
    # R + Round Key:     0xA8830661
    # S-Box Application: 0x303174FA
    # Shift Left:        0x8BA7D181
    #
    # Do not worry if you are not able to reproduce this encryption,
    # just carry on with the rest of this assignment.

def plaintextAvalance():
    print('\nAvalance effect for changes in plaintext.')
    print('Original difference: %d' %
          bitDifference(plaintext0, plaintext1))
    for rounds in xrange(32):
        c0 = gostEncrypt(plaintext=plaintext0, key=key0, rounds=rounds)
        c1 = gostEncrypt(plaintext=plaintext1, key=key0, rounds=rounds)
        print('Round: %02d Delta: %d' % (rounds+1, bitDifference(c0, c1)))

def keyAvalance():
    print('\nAvalance effect for changes in key.')
    print('Original difference: %d' % 
          bitDifference(plaintext0, plaintext0))
    for rounds in xrange(32):
        c0 = gostEncrypt(plaintext=plaintext0, key=key0, rounds=rounds)
        c1 = gostEncrypt(plaintext=plaintext0, key=key1, rounds=rounds)
        print('Round: %02d Delta: %d' % (rounds+1, bitDifference(c0, c1)))

testEncrypt()
#plaintextAvalance()
#keyAvalance()