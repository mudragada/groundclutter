
def multiplesOfThreeAndFive(val):
	return str(sum(i for i in range(val) if (i%3 == 0 or i%5 ==0)))

if __name__ == "__main__":
	val = input("Enter your range: ") 
	print(multiplesOfThreeAndFive(int(val)))