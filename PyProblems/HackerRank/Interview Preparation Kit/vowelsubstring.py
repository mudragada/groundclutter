import time

class Solution:
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING s
    #  2. INTEGER k
    def find_Substring(self, s, k):
        pos = 0
        maxCount = 0
        bestStr=''
        while(pos+k <= len(s)):
            substr = s[pos:pos+k]

            counter = 0
            for char in substr:
                if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                    counter += 1
            if (maxCount < counter):
                maxCount = counter
                bestStr = substr
            pos += 1
        if(bestStr == ''):
            bestStr = 'Not found!'
        return bestStr

    def findSubstring(self, s, k):
        start = time.time()
        pos=0
        maxCount=0
        bestStr=''
        while(pos+k <= len(s)):
            substr = s[pos:pos+k]
            subStrCount = self.countVowels(substr)
            if(maxCount < subStrCount):
                maxCount = subStrCount
                bestStr = substr
            pos += 1
        if(bestStr == ''):
            bestStr = 'Not found!'
        end = time.time()
        return bestStr

    def countVowels(self,s):
        count=0
        for char in s:
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                count += 1
        return count

    # Write your code here
def main():
    sObj = Solution()
    testArr1 = ['caberqiitefg', 'aeiouia', 'azerdii', 'qwdftr']
    testArr2 = [5,3,5,2]
    ansArr = ['erqii', 'aei', 'erdii', 'Not found!']
    for index in range(0, len(testArr1)):
        message = "failed"
        end = 0
        start = time.time()
        if(sObj.find_Substring(testArr1[index], testArr2[index]) == ansArr[index]):
            end = time.time()
            message = "success in " + str(round((end-start)*1000,5)) + " ms"
        else:
            end = time.time()
            message = "failed in " + str(int((end-start)*1000)) + " ms"
        print("Test case " + str(index) + ": " + message)


if __name__ == "__main__":
    main()
