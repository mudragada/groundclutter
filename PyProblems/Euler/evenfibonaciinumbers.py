"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def sumEvenFibonacci(limit):
	startNum = 1
	nextNum = 2
	sumOfEvens = 0
	while startNum <= limit:
		if startNum%2 == 0:
			sumOfEvens += startNum

		startNum, nextNum = nextNum, startNum + nextNum

	return sumOfEvens

if __name__ == "__main__":
	limit = input("Enter a limit:")
	print(sumEvenFibonacci(int(limit)))