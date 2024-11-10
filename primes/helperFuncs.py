"""General supporting functions."""

squaresUnder960 = {
    0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
    289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900}

def gcd(n, k):
    """Return the GCD of two integers via the Euclidean algorithm."""
    while k:
        n, k = k, n%k

    return abs(n)

def isIntegerSquare(N):
    """Determine if N is a perfect square."""
    if N <= 960:
        return N in squaresUnder960

    numZeros = len(str(N)) // 2
    a = int('1'+'0'*numZeros)
    b = (a**2 + N)//(2*a)
    while abs(a-b) > 5:
        a, b = b, (b**2 + N)//(2*b)

    res = False; diff = N - b**2
    if diff == 0:
        res = True
    elif abs(diff-1) == 2*b:
        res = True
            
    return res

def v_2(N):
    """Return the 2-adic valution of N."""
    if N == 0:
        res = float('inf')
    else:
        res = 0
        while N&1 == 0:
            res += 1
            N >>= 1
        
    return res, N

def v_p(N, p):
    """Return the p-adic valution of N."""
    if p == 2:
        return v_2(N)
    res = 0
    if N == 0:
        res = float('inf')
    else:
        while (N % p == 0):
            res += 1
            N //= p

    return res, N

def jacobiSymbol(a, N):
    """Return the Jacobi symbol of two numbers (N > 0 and N%2 == 1)."""
    a %= N
    sgn = 1
    while a != 0:
        pow2, a = v_2(a)
        if pow2%2 == 1 and N%8 in {3, 5}:
            sgn *= -1
            
        a, N = N, a
        if a%4 == 3 and N%4 == 3:
            sgn *= -1
            
        a %= N

    return sgn if N==1 else 0
