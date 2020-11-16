class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                twoSome = nums[i] + nums[j]
                print("i=" + str(i) + " j=" + str(j) + " twoSum = " + str(twoSome))
                if (twoSome == target and i!=j):
                    return [i,j]
        return []



def main():
    sObj = Solution()
    target = 6
    nums = [3,2,4]
    returnObj = sObj.twoSum(nums, target)
    if(returnObj):
        print(returnObj)
    else:
        print("None matched")

if __name__ == "__main__":
    main()
