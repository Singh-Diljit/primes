"""Test strongLucas.py"""

import unittest
import sys
sys.path.append('../primes')
from helperFuncs import *

def slowLucas(P, Q, k):
    """Generate the k+1 term of U, V (k >= 2 and even) taken mod(k-1)."""
    m = k-1
    U = [0, 1]
    V = [2, P]
    iterate = lambda seq: P*seq[1] - Q*seq[0]
    for i in range(2, k+1):
        U = [U[1], iterate(U)]
        V = [V[1], iterate(V)]

    return U[1]%m, V[1]%m

def fastLucas(P, Q, k):
    """Generate the k+1 term of U, V (k >= 2 and even) taken mod(k-1)."""
    m = k-1
    D = P**2 - 4*Q
    pow2, d = v_2(k)
    powQ = Q
    u, v = 1, P%m

    nextU = lambda u, v: (P*u+v)//2 if (P*u+v)%2==0 else (P*u+v+m)//2
    nextV = lambda u, v: (D*u+P*v)//2 if (D*u+P*v)%2==0 else (D*u+P*v+m)//2
    for i in bin(d)[3:]:
        u, v = (u*v)%m, (v**2 - 2*powQ)%m
        powQ = pow(powQ, 2, m)
        if i == '1':
            u, v = nextU(u, v)%m, nextV(u, v)%m
            powQ = (powQ * Q)%m


    for _ in range(pow2):
        u, v = (u*v)%m, (v**2 - 2*powQ)%m
        powQ = pow(powQ, 2, m)

    return u, v

class TestStrongLucas(unittest.TestCase):

    def test_binScheme(self):
        """Test the (implicit) binary scheme used to generate U_k and V_k."""
        for x in range(2, 100, 2): #in the function x would be positive, even.
            pow2, d = v_2(x)
            x_build = 1
            for i in bin(d)[3:]:
                x_build *= 2
                if i == '1': x_build += 1

            #Check if odd part of x was reached.  
            self.assertEqual(x_build, d)

            for i in range(pow2): x_build *= 2
            #Check if full value was reached.
            self.assertEqual(x_build, x)

    def test_LucasSeq(self):
        """Test the implemented quick generation of U_k and V_k."""
        for P in range(-3, 3):
            for Q in range(-3, 3):
                for k in range(10, 20, 2):
                    self.assertEqual(slowLucas(P, Q, k), fastLucas(P, Q, k))

if __name__ == '__main__':
    unittest.main()
