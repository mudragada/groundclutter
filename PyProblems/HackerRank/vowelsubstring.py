
import time

class Solution:
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING s
    #  2. INTEGER k

    def maxVowels(self, s, k):
        strlen = len(s)
        vcount = 0
        maxcount = 0
        bestStr = ''
        for i in range(0,k):
            if(s[i] in 'aeiou'):
                vcount += 1
        if(maxcount < vcount):
            maxcount = vcount
            bestStr = s[0:k]

        for pos in range(1, strlen-k+1):
            if(s[pos+k-1] in 'aeiou'):
                vcount += 1
            if(s[pos-1] in 'aeiou' and vcount > 0):
                vcount -= 1
            if(maxcount < vcount):
                maxcount = vcount
                bestStr = s[pos:pos+k]
        if(bestStr == ''):
            bestStr = 'Not found!'

        return bestStr

def main():
    sObj = Solution()
    testArr1 = ['abciiidef','caberqiitefg', 'aeiouia', 'azerdii', 'qwdftr']
    testArr2 = [3,5,3,5,2]
    ansArr = ['iii','erqii', 'aei', 'erdii', 'Not found!']

    for index in range(0, len(testArr1)):
        message = "failed"
        end = 0
        start = time.time()
        if(sObj.findSubStringSlidingWindow(testArr1[index], testArr2[index]) == ansArr[index]):
            end = time.time()
            message = "SlidingWindow success in " + str(round((end-start)*1000,6)) + " ms"
        else:
            end = time.time()
            message = "SlidingWindow failed in " + str(round((end-start)*1000,6)) + " ms"
        print("Test case " + str(index) + ": " + message)

if __name__ == "__main__":
    main()
