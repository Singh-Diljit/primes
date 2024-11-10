"""Implementation of Lenstra's elliptic-curve factorization (speed focused)."""

from random import randint

# Functions for modular inverses

def extGCD(N, M):
    """Return the GCD and Bezout coefficients of two integers.

    Parameters
    ----------
    N, M : int : Non-zero integers, order does not matter.

    Returns
    -------
    A 3-tuple of ints: (a, b, c) such that N*a + M*b = gcd(N, M) = c.

    Example(s)
    ----------
    >>> extGCD(15, 2)
    >>> (1, -7, 1)

    >>> extGCD(12, 14)
    >>> (-1, 1, 2)
    
    """
    prevX, X = 0, 1
    prevY, Y = 1, 0
    while N != 0:
        (q, N), M = divmod(M, N), N
        prevY, Y = Y, prevY - q*Y
        prevX, X = X, prevX - q*X

    return prevX, prevY, M

def modInv(N, M):
    """Attempt to find the multiplicative inverse of an element in Z/MZ.

    Parameters
    ----------
    N : int : Number to be inverted (not required to be principal value).
    M : int : Modulus being considered.

    Returns
    -------
    A 2-tuple of the form (exists, res).
    
    exists : bool : If the element is invertible.
    res    : int  : If invertible the inverse else the obstruction (=gcd(n,m)).

    Example(s)
    ----------
    >>> modInv(2, 6)
    >>> (False, 2)

    >>> modInv(3, 8)
    >>> (True, 3)
    
    """
    N %= M
    N, _, gcf = extGCD(N, M)
    return (True, N%M) if (gcf == 1) else (False, gcf)

# Elliptic curve operations

def double(x, y, a, M):
    """Attempt to return 2P.

    Parameters
    ----------
    x : int, float : x-coordinate of a point on the curve.
    y : int        : y-coordinate of a point on the curve.
    a : int        : Used to define the curve.
    M : int        : The modulus.

    Returns
    -------
    A 3-tuple of the form (exists, resX, resY).
    
    exists : bool       : If 2P is well-defined.
    resX   : int, float : If exists x-coordinate of 2P else the obstruction.
    resY   : int        : If exists y-coordinate of 2P else -1.
    
    """
    if x == float('inf'): #ord(P) = 1
        exists, resX, resY = True, x, y

    elif (y == 0) or (2*y % M == 0): #ord(P) = 2
        exists, resX, resY = True, float('inf'), -1

    else: #general doubling
        exists, dyInv = modInv(2*y, M)
        if not exists:
            resX, resY = dyInv, -1
        else: 
            slope = (3*x**2+a)%M * dyInv
            resX = (slope**2 - 2*x) % M
            resY  = (slope*(x-resX) - y) % M
    
    return exists, resX, resY

def add(pX, pY, qX, qY, a, M):
    """Attempt to return the sum of two points.

    Parameters
    ----------
    pX, pY : int : Represent a point on the curve.
    qX, qY : int : Represent a point on the curve.
    a      : int : Used to define the curve.
    M      : int : The modulus.

    Returns
    -------
    A 3-tuple of the form (exists, resX, resY).
    
    exists : bool       : If sum is well-defined.
    resX   : int, float : If exists x-coordinate of sum else the obstruction.
    resY   : int        : If exists y-coordinate of sum else -1.
    
    """
    exists = None
    if pX == float('inf'): #P is the identity
        exists, resX, resY = True, qX, qY

    elif qX == float('inf'): #Q is the identity
        exists, resX, resY = True, pX, pY
    
    elif pX == qX: #Check if P == Q or P == -Q
        if (pY + qY) % M == 0:
            exists, resX, resY = True, float('inf'), -1

        elif pY == qY:
            exists, resX, resY = double(pX, pY, a, M)
            return double(pX, pY, a, M)
        
    if exists is None: #general addition
        exists, dxInv = modInv(qX-pX, M)
        if not exists:
            resX, resY = dxInv, -1
        else: 
            slope = (dxInv * (qY-pY)) % M
            resX = (slope**2 - pX - qX) % M
            resY = (slope*(pX-resX) - pY) % M
    
    return exists, resX, resY

def mult(x, y, k, a, M):
    """Attempt to return kP.

    Parameters
    ----------
    x : int, float : x-coordinate of a point on the curve.
    y : int        : y-coordinate of a point on the curve.
    k : int        : Scaler multiple.
    a : int        : Used to define the curve.
    M : int        : The modulus.

    Returns
    -------
    A 3-tuple of the form (exists, resX, resY).
    
    exists : bool       : If kP is well-defined.
    resX   : int, float : If exists x-coordinate of kP else the obstruction.
    resY   : int        : If exists y-coordinate of kP else -1.
    
    """
    exists = None
    if (k == 0) or (x == float('inf')): #Result is trivially the identity
        return True, float('inf'), -1
    
    if k < 0: #-|k|P = k(-P)
        k *= -1
        y = (M - y if y != 0 else 0)

    #Perform multiplication
    exists, resX, resY = True, float('inf'), -1
    for bit in bin(k)[:1:-1]:
        if bit == '1':
            exists, resX, resY = add(x, y, resX, resY, a, M)
            if not exists: return exists, resX, resY
        
        exists, x, y = double(x, y, a, M)
        if not exists: return exists, resX, resY

    return exists, resX, resY

# Lenstra

def factorial(n):
    """Return n!."""
    return 1 if (n in {0, 1}) else n*factorial(n-1)

def lenstra(N, bound=500, effort=500):
    """Attempt to return a factor of N.

    Parameters
    ----------
    N     : int : Integer whose factor is to be found.
    bound : int : [bound!]P for some point P on an EC is computed.
    effort: int : Maximum times EC mult is attempted.

    Returns
    -------
    res : int : A factor of N (res=N, if factor can't be found).

    Example(s)
    ----------
    >>> N = (3209622181 * 6727426213 * 2810645183)
    >>> lenstra(N)
    >>> 2810645183 #Result may vary

    """
    num, searching = factorial(bound), True
    randInts = [randint(0, N-1) for _ in range(3*effort)]
    for i in range(effort):
        if not searching: break
        x, y, a = randInts[i:i+3]
        searching, x, y = mult(x, y, num, a, N)
        
    return N if searching else x
