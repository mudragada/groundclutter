"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


"""
Solution is based on two facts.
1. Every composite number has at least one prime factor less than or equal to square root of itself.
2. 2 is the only even prime number. All other prime numbers are odd.

Solution
1. if the given number is even, reduce it to the nearest odd.
2. If the given number ends with 5, reduce it to the nearest odd.
3. If the number is <2, then return the num (Though 0 or 1 is not the right solution)
5. If the number is 2, then return the num
6. From 3 to sqrt(reduced_number), find a prime factor. If you can't the reduced_number itself is prime
"""

import math
import time
def breakDownToLowestOdd(num):
    if(num>=2):
        while(num%2==0):
            num /= 2
    return num
def breakDownToLowestNonFive(num):
    if(num>=5):
        while(num%5==0):
            num /= 5
    return num


def largestPrimeFactor(num):
    prime_list = []
    if(num>=2):
        num = int(breakDownToLowestOdd(num))
        if (num == 1):
            return 2
        num = int(breakDownToLowestNonFive(num))
        if (num == 1):
            return 5
    else:
        return num
    max = int(math.sqrt(num)) + 1
    for i in range(3, max, 2):
        while (num % i == 0):
            if(i not in prime_list):
                prime_list.append(i)
            num = int(num/i)
    if(num>=3 and num not in prime_list):
        prime_list.append(num)
    return prime_list[len(prime_list)-1]

def main():
    start = time.time()
    number = input("Enter a number:")
    print(largestPrimeFactor(number))
    finish = time.time()
    print("Executed in ", round((finish-start)*1000,6), "ms")

if __name__ == '__main__':
    main()
