"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""

import time

class Solution:
    def repeatedString(self, s,n):
        strlen = len(s)
        numvowels = 0
        for char in s:
            if(char == 'a'):
                numvowels += 1
        remainder = n%strlen
        if(remainder > 0):
            remainderStr = s[0:remainder]
        else:
            remainderStr = ''
        remainderVowels = 0
        for char in remainderStr:
            if(char == 'a'):
                remainderVowels += 1
        return (int(n/strlen)*numvowels + remainderVowels)

def main():
    sObj = Solution()
    testArr1 = ['abcac','aba', 'a']
    testArr2 = [10,10,100000]
    ansArr = [4,7,100000]

    for index in range(0, len(testArr1)):
        message = "failed"
        end = 0
        start = time.time()
        if(sObj.repeatedString(testArr1[index], testArr2[index]) == ansArr[index]):
            end = time.time()
            message = "SlidingWindow success in " + str(round((end-start)*1000,6)) + " ms"
        else:
            end = time.time()
            message = "SlidingWindow failed in " + str(round((end-start)*1000,6)) + " ms"
        print("Test case " + str(index) + ": " + message)

if __name__ == "__main__":
    main()
