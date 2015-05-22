#!/usr/bin/env sage
# -*- coding: utf-8 -*-

# Implemented the Simplified AES algorithm as described in
# Stalling's book and the following paper:
# <https://stud.fh-wedel.de/handout/Beuster/ss2015/crypto/s-aes-spec.pdf>
#
# Hint: A detailed walk-through of an encryption and a decryption
# operation is given in the following paper:
# <https://stud.fh-wedel.de/handout/Beuster/ss2015/crypto/CSS322Y12S2H02-Simplified-AES-Example.pdf>

def xor(a, b):
    def h(x,y):
        if(x==y):
            return(0)
        else:
            return(1)
    return(map(lambda (x, y): h(x,y), zip(a,b)))


def int2blist(n, length):
    b = bin(n)
    l = string2blist(b[2:])
    return([0]*(length-len(l)) + l)
    
def string2blist(s):
    return(map(int, list(s)))

def pp(b):
    """Pretty print bit lists"""
    t = "".join(map(str, b))
    r = ""
    for i in xrange(0, len(t), 4):
        r += t[i:i+4] + ' '
    return(r)

# Since the mix column operations are tricky, the following
# implementations are provided for your convenience.
    
def mix_col(d, inv=False):
    L.<a> = GF(2^4);
    V = VectorSpace(GF(2),8)
    if inv:
        MixColumns_matrix = Matrix(L, [[a^3+1,a],[a,a^3+1]])
    else:
        MixColumns_matrix = Matrix(L, [[1,a^2],[a^2,1]])
    d0 = d[0:4]
    d0.reverse()
    d1 = d[4:8]
    d1.reverse()
    d2 = d[8:12]
    d2.reverse()
    d3 = d[12:16]
    d3.reverse()
    dMatrix = Matrix(L, [[d0, d2],
                         [d1, d3]])
    matrixProduct = MixColumns_matrix*dMatrix
    r = []
    for j in xrange(2):
        for i in xrange(2):
            r += int2blist(int(matrixProduct[i][j].int_repr()), 4)
    return(r)

def inv_mix_col(d):
    return(mix_col(d=d, inv=True))

# You probably want to define more utility functions

##################
# YOUR CODE HERE #
##################

def saes_encrypt(plaintext, key):
    pass
##################
# YOUR CODE HERE #
##################

def saes_decrypt(ciphertext, key):
    pass
##################
# YOUR CODE HERE #
##################

def test():
    for (plaintext, key, ciphertext) in [
         (# Stallings, Exercise 5.10 / 5.12 / 5.14
          '0110111101101011',
          '1010011100111011',
          '0000011100111000')
        ,(# Gordon
          '1101011100101000',
          '0100101011110101',
          '0010010011101100')
        ,(# Holden
          '0110111101101011',
          '1010011100111011',
          '0000011100111000')
        ]:
        plaintext = string2blist(plaintext)
        ciphertext = string2blist(ciphertext)
        key = string2blist(key)
        assert(saes_encrypt(plaintext=plaintext, key=key)
               == ciphertext)
        assert(saes_decrypt(ciphertext=ciphertext, key=key)
               == plaintext)

test()
