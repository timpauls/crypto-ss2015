#!/usr/bin/env sage
"""Calculating with Chinese Remainder Theorem"""

# In this assignment, you will use the Chinese Remainder Theorem to do
# some calculations. First, you will have to write a function that
# converts a given integer i in Z_M to a tuple of remainders and back.
#
# In this assignment, we use the following data structure to represent
# the residuals:
#
# [(r_1, m_1), (r_2, m_2), ..., (r_3, m_3)]
#
# For example, Sun Zi's problem is represented as
#
# [(2,3), (3,5), (2,7)]
#
# Hint: sage function factor() factorizes a number into its prime
# factors.

def int2remainder(i, M):
    """Convert an integer number to a list of pairs (residual, modulus).

    M shall be the product of the moduli, i.e. M=m_1;\ldots;m_n."""
    pass
##################
# YOUR CODE HERE #
##################

def remainder2int(chineseRemainder):
    """Convert a list of pairs (residual, modulus) to an integer."""
    pass
##################
# YOUR CODE HERE #
##################

def remainderAdd(a, b, M):
    """Calculate (a+b) % M using the Chinese Remainder Theorem."""
    pass
##################
# YOUR CODE HERE #
##################

def testRepresentation():
    # Lady
    x=[(4,5), (7,8), (3,9)]
    assert(remainder2int(x) == 39)
    # Stallings, p. 280
    x=int2remainder(973,1813)
    assert((remainder2int(x))== 973)
    # Sun Zi
    x=[(2,3), (3,5), (2,7)]
    assert(remainder2int(x) == 23)
    
def testAdd():
    # Stallings, p. 264
    assert(remainderAdd(678, 973, 1813) == (678+973))

if __name__ == "__main__":
    testRepresentation()
    testAdd()
