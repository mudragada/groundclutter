"""
Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer "n", perform the following conditional actions:
    - If "n" is odd, print Weird
    - If "n" is even and in the inclusive range of 2 to 5, print Not Weird
    - If "n" is even and in the inclusive range of 6 to 20, print Weird
    - If "n" is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not "n" is weird.

Input Format
-----------

A single line containing a positive integer, "n".

Constraints
-----------
1<= n <= 100

Output Format
-------------

Print Weird if the number is weird; otherwise, print Not Weird.

"""

#!/bin/python3

import math
import os
import random
import re
import sys


def printWeird(n):
    if(n>0 and n<=100):
        if(n%2 != 0 or (n%2==0 and (n>=6 and n<=20))):
            print("Weird")
        else:
            print("Not Weird")


if __name__ == '__main__':
    printWeird(1) ## Expect "Weird"
    printWeird(2) ## Expect "Not Weird"
    printWeird(4) ## Expect "Not Weird"
    printWeird(5) ## Expect "Weird"
    printWeird(6) ## Expect "Weird"
    printWeird(20) ## Expect "Weird"
    printWeird(19) ## Expect "Weird"
    printWeird(22) ## Expect "Not Weird"
    printWeird(100) ## Expect "Not Weird"
