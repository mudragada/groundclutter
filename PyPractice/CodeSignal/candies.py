"""

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
[Python3] Syntax Tips
"""
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
