"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""
import math
class Solution(object):
    def addTwoNums(self, l1, l2):
        numl1 = 0
        numl2 = 0
        for i in range(0,len(l1)):
            sum = l1[i] * math.pow(10,i)
            numl1 += sum
        for i in range(0, len(l2)):
            sum = l2[i] * math.pow(10, i)
            numl2 += sum
        sumTwo = numl1 + numl2
        sumArr = []
        index = 0
        if(sumTwo > 0):
            while(sumTwo > 0):
                arrNum = int(sumTwo%10)
                sumTwo = int(sumTwo/10)
                sumArr.append(arrNum)
                i += 1
        else:
            sumArr = [0]

        return sumArr



def main():
    sObj = Solution()
    testArr1 = [[2,4,3], [6,8,5], [4,0,0], [0,0,9], [0]]
    testArr2 = [[4,2,6], [8,4,2], [9,8,8], [9,9,1], [0]]
    ansArr = [[6,6,9],[4,3,8],[3,9,8],[9,9,0,1], [0]]

    for i in range(0, len(testArr1)):
        msg = ""
        if(sObj.addTwoNums(testArr1[i], testArr2[i]) != ansArr[i]):
            msg = "failed"
        else:
            msg = "passed"
        print("Test " + str(i) + ": " + msg)

if __name__=="__main__":
    main()
