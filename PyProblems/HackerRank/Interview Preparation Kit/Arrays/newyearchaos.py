import time
class Solution:
    def minimumbribes(self, q):
        chaotic=False
        swaps = 0
        for i in range(len(q)-1,0,-1):
            if(q[i]!=(i+1)):
                if(q[i-1]==(i+1)):
                    swaps += 1
                    q[i-1], q[i] = q[i], q[i-1]
                elif(q[i-2] == i+1):
                    swaps += 2
                    q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
                else:
                    chaotic=True
        if(chaotic):
            return 'Too chaotic'
        else:
            return str(swaps)


def main():
    sObj = Solution()
    testArr1 = [[2,1,5,3,4],[2,5,1,3,4],[1,2,3,5,4,6,7,8],[4,1,2,3]]
    ansArr = ['3','Too chaotic','1','Too chaotic']

    for index in range(0, len(testArr1)):
        message = "failed"
        end = 0
        start = time.time()
        if(sObj.minimumbribes(testArr1[index]) == ansArr[index]):
            end = time.time()
            message = "SlidingWindow success in " + str(round((end-start)*1000,6)) + " ms"
        else:
            end = time.time()
            message = "SlidingWindow failed in " + str(round((end-start)*1000,6)) + " ms"
        print("Test case " + str(index) + ": " + message)

if __name__ == "__main__":
    main()
