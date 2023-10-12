# Define initial MD5 state (A, B, C, D)
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476


# Helper functions for MD5 operations
def F(X, Y, Z):
    return (X & Y) | (~X & Z)


def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)


def H(X, Y, Z):
    return X ^ Y ^ Z


def I(X, Y, Z):
    return Y ^ (X | ~Z)


# Functions for MD5 main rounds
def FF(a, b, c, d, x, s, ac):
    a = (a + F(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a
