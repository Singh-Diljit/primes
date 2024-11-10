"""Prime Counts."""

from deterministicMillerRabin import detMillerRabin
from millerRabin import *
from baillePSW import baillePSW
from time import time

def primeCount(n, func):
    """Count primes below n."""
    cnt = 2
    for x in range(5, n, 2): cnt += func(x)
    return cnt

def timeCount(upper, func):
    """Count primes below n and time taken."""
    cnt = 2; totTime = 0
    for x in range(5, upper):
        start = time()
        a = func(x)
        totTime += time() - start
        cnt += func(x)

    print(f'{func.__name__}: {cnt}: time: {totTime}')
