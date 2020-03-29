###
#n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child.
#Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

## Example

#For n = 3 and m = 10, the output should be
#candies(n, m) = 9.

#Each child will eat 3 pieces. So the answer is 9.
###
def main():
    print(candies(3,0))
    print(candies(3,9))
    print(candies(5,100))

def candies(n, m):
    candylist = [0] * (n)
    while(m > 0 and m>=n):
        for i in range(0, n):
            candylist[i] = candylist[i] + 1
            m = m-1

    print (candylist)
    return sum(candylist)

if __name__ == '__main__':
    main()
