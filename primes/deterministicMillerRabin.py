"""Deterministic Miller-Rabin for N < 3,317,044,064,679,887,385,961,981."""

from helperFuncs import v_2
from specialCases import fastCases

composite = False
isPrime = True

millerRabinCutOffs = {
    2  : 2047,
    3  : 1373653,
    5  : 25326001,
    7  : 3215031751,
    11 : 2152302898747,
    13 : 3474749660383,
    17 : 341550071728321,
    19 : -1,
    23 : 3825123056546413051,
    29 : -1,
    31 : -1,
    37 : 318665857834031151167461,
    41 : 3317044064679887385961981
    }

def detMillerRabin(N):
    """Determine if N < 3,317,044,064,679,887,385,961,981 is prime."""
    looseCheck = fastCases(N)
    if looseCheck != 1:
        return bool(looseCheck)
    
    N_ = N-1
    pow2, oddM = v_2(N_)

    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for p in bases:
        x = pow(p, oddM, N)
        for _ in range(pow2):
            y = pow(x, 2, N)
            if (y == 1) and (x not in {1, N_}):
                return composite
            x = y

        if y != 1:
            return composite

        if N < millerRabinCutOffs[p]:
            break
            
    return isPrime
