"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1sObj. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= numsObj.length <= 105
nums[i] is either 0 or 1.

"""

class Solution:
    def findMaxNumConsecutiveOnes(self, nums):
        start = -1
        end = -1
        maxcon = 0
        for i in range(0, len(nums)):
            if(nums[i] == 1):
                if(start<0):
                    start = i
                end = i
                if(maxcon < (end - start + 1)):
                    maxcon = end - start + 1
            else:
                start = -1
                end = -1

        return maxcon

def main():
    sObj = Solution()
    testArray = [[0], [1], [0,0,0,0,0], [1,1,1,1,1,1], [0,0,0,0,0,0,1], [0,0,0,0,0,0,1], [0,0,1,1,0,1,1,1], [1,0,1,1,0,1,1,1,0]]
    ansArray = [0, 1, 0, 6, 1, 1, 3, 3]
    for i in range(0, len(testArray)):
        tRay = testArray[i]
        if(sObj.findMaxNumConsecutiveOnes(tRay) != ansArray[i]):
            print("Test " + str(i) + ": failed")
        else:
            print("Test " + str(i) + ": passed")


if __name__ == "__main__":
    main()
