"""BaillePSW."""

from helperFuncs import gcd, v_2, isIntegerSquare, jacobiSymbol
from specialCases import fastCases

composite = False
likelyPrime = True

def oddNQR(N, effort=100):
    """Return the first (alternating) odd number that is not a QR mod N."""
    #Proved on avg ~3.1478 tries.
    res = 0
    start, sgn = 5, 1
    for i in range(5, effort+5, 4):
        if jacobiSymbol(i, N) == -1:
            res = i; break
            
        if jacobiSymbol(-i-2, N) == -1:
            res = -i-2; break

    return res

def millerRabin_Baille(N, N_, pow2, oddM):
    """Perform the (base=B) Miller-Rabin primality test."""
    x = pow(2, oddM, N)    
    if x in {1, N_}: #Check if x == +-1 mod(N)
        return likelyPrime
        
    for _ in range(1, pow2): #Check if x**(2**r) == -1 mod(N); 0 < r < pow2
        x = pow(x, 2, N)
        if x == N_:
            return likelyPrime
            
    return composite

def strongLucas_Baille(N, D, Q, pow2, d):
    """Perform the strong Lucas probable prime test."""    
    u, v = 1, 1
    powQ = Q

    nextU = lambda u, v: (u+v)//2 if (u+v)%2==0 else (u+v+N)//2
    nextV = lambda u, v: (D*u+v)//2 if (D*u+v)%2==0 else (D*u+v+N)//2
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

def baillePSW(N, effortNQR=100):
    """Perform the (strong) Baille-PSW test; no known exceptions."""
    looseCheck = fastCases(N)
    if looseCheck != 1:
        return bool(looseCheck)

    NMinus = N-1
    pow2Minus, dMinus = v_2(NMinus)
    if not millerRabin_Baille(N, NMinus, pow2Minus, dMinus):
        return composite

    D = oddNQR(N, effortNQR)
    if gcd(D, N) != 1:
        return composite
    
    Q = (1-D)//4
    NPlus = N+1
    if pow2Minus > 1:
        pow2Plus, dPlus = 1, NPlus//2
    else:
        pow2Plus, dPlus = v_2(NPlus)

    if not strongLucas_Baille(N, D, Q, pow2Plus, dPlus):
        return composite

    return likelyPrime
