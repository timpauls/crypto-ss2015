#!/usr/bin/env sage

E = EllipticCurve(IntegerModRing(13), [1, 6])
G = E(12, 2)
nB = 8

# 1. Bob's public key
PB = G * nB
print "Bob's public key: ", PB
# Bob's public key:  (4 : 10 : 1)

# 2. message encryption
k = 5
M = E(11, 3)
C1 = k * G
C2 = M + k * PB
print "Ciphertext: ", (C1, C2)
# Ciphertext:  ((4 : 3 : 1), (4 : 3 : 1))

# 3. message decryption
X = nB * C1
Md = C2 - X
print "Decrypted message: ", Md
# Decrypted message:  (11 : 3 : 1)