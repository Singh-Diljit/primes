"""Probablistic Miller-Rabin test."""

from helperFuncs import v_2
from specialCases import fastCases
import random

likelyPrime = True
composite = False

def singleMillerRabin(N, B=2):
    """Perform the (base=B) Miller-Rabin primality test."""
    looseCheck = fastCases(N)
    if looseCheck != 1:
        return bool(looseCheck)
    
    res = composite
    N_ = N-1
    pow2, oddM = v_2(N_)
    x = pow(B, oddM, N)
    
    if x in {1, N_}: #Check if x == +-1 mod(N)
        res = likelyPrime
        
    else: #Check if x**(2**r) == -1 mod(N); 0 < r < pow2
        for _ in range(1, pow2):
            x = pow(x, 2, N)
            if x == N_:
                res = likelyPrime; break
            
    return res

def millerRabin(N, numBases=10):
    """Perform the Miller-Rabin primality test for randomly choosen bases."""
    looseCheck = fastCases(N)
    if looseCheck != 1:
        return bool(looseCheck)
    
    N_ = N-1
    pow2, oddM = v_2(N_)
    bases = random.sample(range(2, N-1), numBases)
    for B in bases:
        x = pow(B, oddM, N)
        for _ in range(pow2):
            y = pow(x, 2, N)
            if (y == 1) and (x not in {1, N_}):
                return composite
            x = y

        if y != 1:
            return composite
            
    return likelyPrime  
