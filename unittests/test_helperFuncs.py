"""Test helperFuncs.py"""

import unittest
import sys
sys.path.append('../primes')
from helperFuncs import *

class TestIsIntegerSquare(unittest.TestCase):

    def test_squares(self):
        ans = [True] * 10000
        toCheck = [isIntegerSquare(x**2) for x in range(10000)]
        self.assertEqual(toCheck, ans)

    def test_notSquares(self):
        sqs = {x**2 for x in range(10**3)}
        ans = [False] * (10**6 - len(sqs))
        toCheck = [isIntegerSquare(x) for x in range(10**6) if x not in sqs]
        self.assertEqual(toCheck, ans)

class TestValutions(unittest.TestCase):

    def test_v_p(self):
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            for x in range(1, 1000):
                powP, d = v_p(x, p)
                self.assertTrue(d%p != 0)
                self.assertEqual(p**powP*d, x)
     
if __name__ == '__main__':
    unittest.main()
