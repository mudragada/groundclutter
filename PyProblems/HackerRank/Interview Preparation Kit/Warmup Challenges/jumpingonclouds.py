class Solution:
    def jumpingOnClouds(self, c):
        pos = 0
        hops = 0
        n = len(c)
        c.append(0)
        while (pos < n-1):
    #        print("pos:", pos, "c[pos]:", c[pos], "c[pos+1]:", c[pos+1],"c[pos+2]:", c[pos+2], "hops:", hops)
            if(c[pos] == 0):
                hops += 1
                if(c[pos+2] == 0):
                    pos = pos+2
                else:
                    pos = pos+1
        return hops

def main():

    sObj = Solution()
    testArr = [[0,1,0,0,0,1,0], [0,0,1,0,0,1,0], [0,0,0,0,0], [0,0,0], [0,1,0,1,0], [0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    ansArr = [3, 4, 2, 1, 2, 3, 4]
    # testArr = ["UDDDUDUU", "DDUDUDUDUUUDUDDDDU", "DDUDUDUUDDUDUDUDUDUDUDUUUUU", "DUUDUDUDUDUUDUDUDUDUUDUDUDUDUDUUDUDUD"]
    # ansArr = [1, -2, 3, 3]
    for index in range(0, len(testArr)):
        message = "failed"
        if(sObj.jumpingOnClouds(testArr[index]) == ansArr[index]):
            message = "success"
        print("Test case " + str(index) + ": " + message)

if __name__ == '__main__':
    main()
