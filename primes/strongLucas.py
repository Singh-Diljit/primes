"""Strong Lucas probable prime test."""

from helperFuncs import gcd, v_2, jacobiSymbol
from specialCases import fastCases

composite = False
likelyPrime = True

def strongLucas(N, P, Q):
    """Perform the strong Lucas probable prime test."""
    looseCheck = fastCases(N)
    if looseCheck != 1:
        return bool(looseCheck)

    D = P**2 - 4*Q
    if gcd(D, N) != 1:
        return composite
    
    delta = N - jacobiSymbol(D, N)
    pow2, d = v_2(delta)

    u, v = 1, P%N
    powQ = Q

    nextU = lambda u, v: (P*u+v)//2 if (P*u+v)%2==0 else (P*u+v+N)//2
    nextV = lambda u, v: (D*u+P*v)//2 if (D*u+P*v)%2==0 else (D*u+P*v+N)//2
    for i in bin(d)[3:]:
        u, v = (u*v)%N, (v**2 - 2*powQ)%N
        powQ = pow(powQ, 2, N)
        if i == '1':
            u, v = nextU(u, v)%N, nextV(u, v)%N
            powQ = (powQ * Q) % N
    
    if (u == 0) or (v == 0):
        return likelyPrime

    for _ in range(pow2):
        u, v = (u*v)%N, (v**2 - 2*powQ)%N
        if (v == 0):
            return likelyPrime
        powQ = pow(powQ, 2, N)

    return composite
