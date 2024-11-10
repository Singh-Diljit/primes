# Prime Number Testing and Factorization

This project implements advanced primality testing and factorization methods, showcasing mathematical rigor and efficient algorithms in pure Python. With a focus on demonstrating computational accuracy and algorithmic depth.

## Features

1. **Baille-PSW Primality Test**  
   A powerful probabilistic primality test, the Baille-PSW method is unique in that no counterexamples have been found, and it has been verified for integers up to \(2^{64}\). This implementation combines the Miller-Rabin and Strong Lucas tests, ensuring a robust approach for large integers.

2. **Strong Lucas Primality Test**  
   The Strong Lucas test complements the Miller-Rabin test by checking properties of Lucas sequences. It is particularly effective for numbers that might pass Miller-Rabin tests but fail Lucas tests.

3. **Deterministic Miller-Rabin Test**  
   A Miller-Rabin test with fixed bases that guarantees correctness for inputs below 3,317,044,064,679,887,385,961,981.

4. **Base-B Miller-Rabin Test**  
   This specialized form of the Miller-Rabin test only uses base B, offering a lightweight, fast option for initial primality checks in specific applications.

5. **Random-Base Miller-Rabin Test**  
   Uses random bases for increased accuracy on very large numbers. This implementation allows the user to specify the number of rounds for customizable confidence.

6. **Lenstra Elliptic Curve Factorization**  
   A fast elliptic curve-based factorization method for integers, using elliptic curve properties to find a nontrivial factor. This method is effective for integers with factors with 20-25 digits.

7. **Prime Counting Function**  
   Estimates or calculates the number of primes less than or equal to a given integer. This function can be used in analytic number theory and provides insights into prime density over ranges.

## Project Structure

```
Project Folder/
│
├── primes/
│   ├── baillePSW.py
│   ├── deterministicMillerRabin.py
│   ├── fastECM.py
│   ├── helperFuncs.py
│   ├── millerRabin.py
│   ├── primeCounting.py
│   ├── smallDivisors.py
│   ├── specialCases.py
│   └── strongLucas.py
│
├── unittests/
│   ├── test_baillePSW.py
│   ├── test_detMillerRabin.py
│   ├── test_helperFuncs.py
│   ├── test_smallDivisors.py
│   └── test_strongLucas.py
│
├── .gitignore
├── LICENSE
├── requirements
├── setup
└── README.md

```

## Getting Started

### Prerequisites

This project only relies on standard Python libraries, specifically `random`.

### Usage

Each feature can be used independently by importing the respective module. Below are example usages for each functionality.

#### Example Usage

```python
from baillePSW import baillePSW
from deterministicMillerRabin import detMillerRabin
from millerRabin import singleMillerRabin
from fastECM import lenstra
from primeCounting import primeCount, timeCount

#Build a thousand digit prime
longPrimeDigits = [
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9999999999,
     9999999999, 9999999999, 9999999999, 9999999999, 9998770801
     ]
N_pr = int(str().join(str(digits) for digits in longPrimeDigits))
# Check if a number is prime using Baille-PSW test
>>> baillePSW(N_pr)
>>> True #Under .5 seconds

# Deterministic Miller-Rabin test
>>> detMillerRabin(N_pr)
>>> True #Under 1 seconds

# Base-B Miller-Rabin test
>>> singleMillerRabin(N_pr)
>>> True #Under .5 seconds

# Lenstra Elliptic Curve Factorization
N = (3209622181 * 6727426213 * 2810645183)
>>> lenstra(N)
>>> 2810645183 #Takes ~ (0.5822016000020085 seconds)

# Prime Counting Function
upperBound = 10**6
>>> primeCount(upperBound, detMillerRabin)
>>> 78498

>>> timeCount(upperBound, detMillerRabin)
>>> detMillerRabin: 78498: time: 0.6930286884307861

>>> primeCount(upperBound, singleMillerRabin)
>>> 78525

>>> timeCount(upperBound, singleMillerRabin)
>>> singleMillerRabin: 78525: time: 0.5849635601043701


>>> primeCount(upperBound, baillePSW)
>>> 78498

>>> timeCount(upperBound, baillePSW)
>>> baillePSW: 78498: time: 1.1790602207183838

```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request, or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

