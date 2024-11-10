"""Test smallDivisors.py"""

import unittest
import sys
sys.path.append('../primes')
from smallDivisors import *

class TestsmallDivisors(unittest.TestCase):

    def test_isSmallPrime(self):
        toCheck = {x for x in range(2000) if isSmallPrime(x)}
        self.assertEqual(toCheck, primesUnder1008)
        
    def test_hasSmallDivisor(self):
        ans = {i:-1 for i in range(2, 1000)}
        
        for p in ([2]+oddPrimesUnder100):
            for ip in range(p, 1000, p):
                if ans[ip] == -1:
                    ans[ip] = p
                    
        toCheck = {i: hasSmallDivisor(i) for i in range(2, 1000)}
        self.assertEqual(toCheck, ans)

    def test_hasSmallDivisor_fastCheck(self):
        ans = {i:False for i in range(3, 1000, 2)}
        for p in oddPrimesUnder100:
            for ip in range(p, 1000, 2*p):
                ans[ip] = True
                
        toCheck = {i: hasSmallDivisor_fastCheck(i) for i in range(3, 1000, 2)}
        self.assertEqual(toCheck, ans)

if __name__ == '__main__':
    unittest.main()
