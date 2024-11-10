"""Deal with special (often trivial) cases."""

from smallDivisors import isSmallPrime, hasSmallDivisor_fastCheck
from helperFuncs import isIntegerSquare

composite = 0
likelyPrime = 1
isPrime = 2

def fastCases(N):
    """Using fast tests determine if N is prime, composite, or undetermined."""
    if N == 2: #Catches 2 allowing other functions to forgo even prime cases.
        return isPrime
    
    if (N%2 == 0) or (N==1): #N == 2 was returned as prime above.
        return composite
    
    if isSmallPrime(N, upperBound=1008):
        return isPrime
    
    if N < 1009: #isSmallPrime has found all primes under upperBound=1008.
        return composite
    
    if (N%4 == 1) and isIntegerSquare(N): #Even values already sifted.
        return composite
    
    if hasSmallDivisor_fastCheck(N):
        return composite

    return likelyPrime
