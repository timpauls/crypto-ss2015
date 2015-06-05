#!/usr/bin/env python

"""FIPS 140-2: RNG Power-Up Tests"""

# Asses the quality of your TRNG by running the statistical random
# number generator tests from Chapter 4.9.1 (Power-Up Tests) of "FIPS
# PUB 140-2 - SECURITY REQUIREMENTS FOR CRYPTOGRAPHIC MODULES". The
# document is available on the handout server.

FILENAME='random.dat'

def readRandomBits(filename):
    """Read file and return it as list of bits."""
    rn = []
    rnFile = open(filename, 'rb')
    rn = map(ord, rnFile.read())
    rnFile.close()
    return(reduce(lambda x,y: x+int2bin(y,8), rn, []))

def int2bin(x, n):
    """Convert integer to array of bits.

    x : integer
    n : length of bit array"""
    b = map(lambda x: ord(x)-ord('0'), list(bin(x)[2:]))
    return([0]*(n-len(b)) + b)

def bin2int(b):
    """Convert array of bits to integer."""
    return(int("".join(map(lambda x: chr(x+ord('0')), b)), 2))

def testRandomNumbers(randomBits):
    assert(monobitTest(randomBits))
    assert(pokerTest(randomBits))
    assert(runsTest(randomBits))
    assert(longRunsTest(randomBits))

def monobitTest(randomBits):
    """FIPS 140-2 monobit test"""
    # Count the number of ones in the 20,000 bit stream. Denote this
    # quantity by x.
    #
    # The test is passed if 9725 < x < 10275
    pass
##################
# YOUR CODE HERE #
##################
    
def pokerTest(randomBits):
    """FIPS 140-2 poker test"""
    # Divide the 20000 bit stream into 5000 contiguous 4 bit
    # segments. Count and store the number of occurrences of the 16
    # possible 4 bit values. Denote f[i] as the number of each 4 bit
    # value i where 0 < i < 15.
    #
    # Evaluate the following:
    #                   15
    #                   --
    # x = (16/5000) * ( \  f[i]^2 ) - 5000
    #                   /
    #                   --
    #                  i=0
    #
    # The test is passed if 2.16 < x < 46.17
    #
    # See fips_140_2.pdf, page 39-40
    pass
##################
# YOUR CODE HERE #
##################
    
def runsTest(randomBits):
    """FIPS 140-2 runs test"""
    # A run is defined as a maximal sequence of consecutive bits of
    # either all ones or all zeros that is part of the 20000 bit
    # sample stream. The incidences of runs (for both consecutive
    # zeros and consecutive ones) of all lengths (>= 1) in the
    # sample stream should be counted and stored.
    #
    # The test is passed if the runs that occur (of lengths 1 through
    # 6) are each within the corresponding interval specified in the
    # table below. This must hold for both the zeros and ones (i.e.,
    # all 12 counts must lie in the specified interval). For the
    # purposes of this test, runs of greater than 6 are considered to
    # be of length 6.
    #
    # Length      Required Interval
    # of Run 
    # 1           2343 - 2657
    # 2           1135 - 1365
    # 3            542 -  708
    # 4            251 -  373
    # 5            111 -  201
    # 6+           111 -  201
    #
    # See fips_140_2.pdf, page 40
    pass
##################
# YOUR CODE HERE #
##################
    
def longRunsTest(randomBits):
    """FIPS 140-2 long runs test"""
    # A long run is defined to be a run of length 26 or more (of
    # either zeros or ones). On the sample of 20000 bits, the test is
    # passed if there are no long runs.
    #
    # See fips_140_2.pdf, page 40
    pass
##################
# YOUR CODE HERE #
##################
    

if __name__ == "__main__":
    randomBits = readRandomBits(filename=FILENAME)
    testRandomNumbers(randomBits=randomBits)
