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

def sbox(nibble):
  values =  [ '1001', '0100', '1010', '1011', '1101', '0001', '1000', '0101',
              '0110', '0010', '0000', '0011', '1100', '1110', '1111', '0111']
  out = string2blist(values[int("".join(map(str, nibble)), 2)])
  return out

def rotNib(word):
  return word[4:] + word[:4]

def subNib(word):
  return sbox(word[:4]) + sbox(word[4:])

def expandKey(key):
  keys = [0] * 3

  w0 = key[:8]
  w1 = key[8:]
  keys[0] = key

  w2 = xor(xor(w0, string2blist('10000000')), subNib(rotNib(w1)))
  w3 = xor(w2, w1)
  keys[1] = w2 + w3

  w4 = xor(xor(w2, string2blist('00110000')), subNib(rotNib(w3)))
  w5 = xor(w4, w3)
  keys[2] = w4 + w5

  return keys

##################
# YOUR CODE HERE #
##################

def saes_encrypt(plaintext, key):
  keys = expandKey(key)

  # -- ROUND 0 --
  round0 = xor(plaintext, keys[0])


  # -- ROUND 1 --
  sboxed = []
  for i in xrange(0, len(round0), 4):
    sboxed += sbox(round0[i:i+4])
  
  # swap 2nd and 4th nibble
  shifted = sboxed[0:4] + sboxed[12:16] + sboxed[8:12] + sboxed[4:8]
  
  #mix columns
  mixed = mix_col(shifted)
  
  # add key
  round1 = xor(mixed, keys[1])
  

  # -- ROUND 2 --
  sboxed = []
  for i in xrange(0, len(round1), 4):
    sboxed += sbox(round1[i:i+4])
  
  # swap 2nd and 4th nibble
  shifted = sboxed[0:4] + sboxed[12:16] + sboxed[8:12] + sboxed[4:8]
  
  # add key
  round2 = xor(shifted, keys[2])
  
  return round2

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