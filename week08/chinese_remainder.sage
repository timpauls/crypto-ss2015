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
    result = []
    for base, exponent in factor(M):
        result.append((i % base**exponent, base**exponent))

    return result

def remainder2int(chineseRemainder):
    """Convert a list of pairs (residual, modulus) to an integer."""
    summands = []
    moduliProduct = 1
    j = var('j')

    for i, pair in enumerate(chineseRemainder):
        otherPairs = chineseRemainder[:i] + chineseRemainder[i+1:]
        product = reduce(lambda x, y: x*y[1], otherPairs, 1)

        summands.append(product * int(solve_mod([j*product==pair[0]], pair[1])[0][0]))
        moduliProduct *= pair[1]

    return sum(summands)%moduliProduct

def remainderAdd(a, b, M):
    """Calculate (a+b) % M using the Chinese Remainder Theorem."""
    return remainder2int(int2remainder(a+b, M))

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