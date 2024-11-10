"""Test the Baille-PSW test."""

import unittest
import sys
sys.path.append('../primes')
from baillePSW import baillePSW

exactPrimeCounts = {
    2: 25,
    4: 1229,
    6: 78498,
    7: 664579}

def BPSWCount(pow10):
    """Count number of primes via BaillePSW"""
    res = 1
    for x in range(1, 10**pow10, 2):
        res += baillePSW(x)
    return res

class TestBaillePSW(unittest.TestCase):

    def test_evens(self):
        """Test result on evens."""
        self.assertEqual(True, baillePSW(2))
        for x in range(4, 1000, 2):
            self.assertEqual(False, baillePSW(x))
            
    def test_numPrimesUnder10_2(self):
        """Count the numebr of primes under 10**2"""
        toCheck = BPSWCount(2)
        self.assertEqual(toCheck, exactPrimeCounts[2])

    def test_numPrimesUnder10_4(self):
        """Count the numebr of primes under 10**4"""
        toCheck = BPSWCount(4)
        self.assertEqual(toCheck, exactPrimeCounts[4])
        
    def test_numPrimesUnder10_6(self):
        """Count the numebr of primes under 10**6"""
        toCheck = BPSWCount(6)
        self.assertEqual(toCheck, exactPrimeCounts[6])

    def test_numPrimesUnder10_7(self):
        """Count the numebr of primes under 10**7"""
        toCheck = BPSWCount(7)
        self.assertEqual(toCheck, exactPrimeCounts[7])
        
if __name__ == '__main__':
    unittest.main()
