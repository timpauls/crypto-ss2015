#!/usr/bin/env sage

# In this exercise, you will get some idea how hard prime
# factorization is.  First you are going to create composite numbers
# from two prime numbers.  Then, you will factorize these numbers and
# measure the time.

import time

def generateN(b):
    """Generates a b-bits number n=p*q where p and q are prime numbers."""
    # For this assignment, generate a composite number n from two
    # random prime numbers p and q. Your number b shall consist of
    # b binary digits. For example, the decimal number 17 has 5 binary
    # digits, because its binary representation is 10001.
    #
    # Hint: Use Sage function random_prime to generate random primes.
##################
# YOUR CODE HERE #
##################
    return(n)
   

def timeToFactor(n):
    """Returns the time in seconds it takes to factor n."""
    # For this assignment, return the time in seconds it takes
    # to factorize composite number n into its prime factors p and q.
    #
    # Hint: Use Sage function factor() for the actual factorization.
    # Use Python function time.clock() to get the time in seconds.
    pass
##################
# YOUR CODE HERE #
##################


def measureTime():
    for i in range(150,310,10):
        n = generateN(i)
        print('Factoring a %d bits number took %.2f seconds.'
              % (i, timeToFactor(n)))

measureTime()
