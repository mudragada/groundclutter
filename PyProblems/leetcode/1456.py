"""
1456. Maximum Number of Vowels in a Substring of Given Length


Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

"""
import time
class Solution(object):
    def maxVowels(self, s, k):
        strlen = len(s)
        vcount = 0
        maxcount = 0
        for i in range(0,k):
            if(s[i] in 'aeiou'):
                vcount += 1
        if(maxcount < vcount):
            maxcount = vcount

        for pos in range(1, strlen-k+1):
            if(s[pos+k-1] in 'aeiou'):
                vcount += 1
            if(s[pos-1] in 'aeiou' and vcount > 0):
                vcount -= 1
            if(maxcount < vcount):
                maxcount = vcount

        return maxcount

def main():
    sObj = Solution()
    testArr1 = ['abciiidef','caberqiitefg', 'aeiouia', 'azerdii', 'qwdftr']
    testArr2 = [3,5,3,5,2]
    ansArr = [3,3,3,3,0]

    for index in range(0, len(testArr1)):
        message = "failed"
        end = 0
        start = time.time()
        if(sObj.maxVowels(testArr1[index], testArr2[index]) == ansArr[index]):
            end = time.time()
            message = "SlidingWindow success in " + str(round((end-start)*1000,6)) + " ms"
        else:
            end = time.time()
            message = "SlidingWindow failed in " + str(round((end-start)*1000,6)) + " ms"
        print("Test case " + str(index) + ": " + message)

if __name__ == "__main__":
    main()
