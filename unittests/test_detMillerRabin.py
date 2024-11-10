"""Test the Deterministic Miller-Rabin test."""

import unittest
import sys
sys.path.append('../primes')
from deterministicMillerRabin import *

exactPrimeCounts = {
    2: 25,
    4: 1229,
    6: 78498,
    7: 664579}

def dMRCount(pow10):
    """Count number of primes via detMillerRabin"""
    res = 1
    for x in range(1, 10**pow10, 2):
        res += detMillerRabin(x)
    return res

class TestMillerRabin(unittest.TestCase):

    def test_evens(self):
        """Test result on evens."""
        self.assertEqual(True, detMillerRabin(2))
        for x in range(4, 1000, 2):
            self.assertEqual(False, detMillerRabin(x))
            
    def test_numPrimesUnder10_2(self):
        """Count the numebr of primes under 10**2"""
        toCheck = dMRCount(2)
        self.assertEqual(toCheck, exactPrimeCounts[2])

    def test_numPrimesUnder10_4(self):
        """Count the numebr of primes under 10**4"""
        toCheck = dMRCount(4)
        self.assertEqual(toCheck, exactPrimeCounts[4])
        
    def test_numPrimesUnder10_6(self):
        """Count the numebr of primes under 10**6"""
        toCheck = dMRCount(6)
        self.assertEqual(toCheck, exactPrimeCounts[6])

    def test_numPrimesUnder10_7(self):
        """Count the numebr of primes under 10**7"""
        toCheck = dMRCount(7)
        self.assertEqual(toCheck, exactPrimeCounts[7])
        
if __name__ == '__main__':
    unittest.main()
