import math
def main():
    while(True):
        print("Enter a number")
        inputNumber = input()
        if(inputNumber == reverseNum(inputNumber)):
            print(str(inputNumber) + " is a palindrome")
        else:
            print(str(inputNumber) + " is not a palindrome")

def reverseNum(num):
    recursiveNum = (num%10 * int(math.pow(10, int(math.log(num,10))))) + checkForPalindrome(num//10)
    return (int(num!=0) and recursiveNum)

if __name__ == "__main__":
    main()
