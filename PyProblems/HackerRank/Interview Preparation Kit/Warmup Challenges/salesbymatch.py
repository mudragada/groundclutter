"""
https://www.hackerrank.com/challenges/counting-valleys/problem

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

*** Example ***
----------------
n = 7
ar = [1,2,1,2,1,3,2]


There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
-------------------------
* Function Description *
--------------------------

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock

---------------
*** Returns ***
----------------
int: the number of pairs

----------------
* Input Format *
----------------

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers, , the colors of the socks in the pile.

--------------
* Constraints *
--------------

 1 <= n <= 100
 1 <= ar[i] <= 100 where 0<= i < n

"""

class Solution:
    def sockMerchant(self, n, ar):
        arrDict =  {}
        numPairs = 0
        for i in range(0,n):
            if ar[i] in arrDict.keys():
                arrDict[ar[i]] += 1
            else:
                arrDict[ar[i]] = 1

        for key in arrDict:
            print("Num pairs for " + str(key) + " = " + str(int(arrDict[key]/2)))
            numPairs += int((arrDict[key])/2)
        return numPairs

def main():
    sObj = Solution()
    testArr = [[1,1,2,2,3], [11, 12, 13, 0, 12, 34, 1], [12, 12, 12, 12, 12], [99, 99, 9, 9, 0]]
    ansArr = [2, 1, 2, 2]
    for index in range(0, len(testArr)):
        message = "failed"
        if(sObj.sockMerchant(len(testArr[index]), testArr[index]) == ansArr[index]):
            message = "success"
        print("Test case " + str(index) + ": " + message)


if __name__ == "__main__":
    main()
