"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
"""

import math
from random import seed
from random import randint

def centuryFromYear(year):
    century = math.ceil(year/100)
    return century

def main():
    for i in range(0,10):
        year = randint(0, 2000)
        printstr = "Century of the year {0} is {1}".format(str(year), str(centuryFromYear(year)))
        print(printstr)

if __name__ == '__main__':
    main()
