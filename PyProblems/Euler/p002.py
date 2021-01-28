"""
Print even fibonacci below a number
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
