"""
Objective
--------
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

Task
----
Given a string,"S", of length "N" that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example
-------
S = adbecf

output: abc def

Input Format
------------

The first line contains an integer,"T"(the number of test cases).
Each line of the subsequent lines contain a string,"S".

Constraints
-----------
1 <= T <= 10
2 <= length of S <= 10000

Output Format
-------------

For each String S(j) (where 0<= j <= T-1), print S(j)'s even-indexed characters, followed by a space, followed by S(j)'s odd-indexed characters.

Sample Input
-----------

2
Hacker
Rank

Sample Output
------------

Hce akr
Rn ak
"""

class Solution:
    def printEvensAndOdds(self, testStrs):
        for testStr in testStrs:
            evenStr = ''
            oddStr = ''
            for i in range(0, len(testStr)):
                if(int(i%2)==0):
                    evenStr = evenStr + testStr[i]
                else:
                    oddStr = oddStr + testStr[i]
            print(str(evenStr) + ' ' + str(oddStr))


def main():
    sObj = Solution()
    t= int(input())
    testStrs = []
    for i in range(0,t):
        testStr= str(input())
        testStrs.append(testStr)
    sObj.printEvensAndOdds(testStrs)

if __name__ == "__main__":
    main()
