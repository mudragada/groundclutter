## Replicating SieveOfEratosthenes
import math

def exitOnError(errMsg):
    print(errMsg)
    exit()

def printAllPrimes(numToPrintAllPrimes):
    print("I will print all prime numbers until " + str(numToPrintAllPrimes) + " ....")
    primeArr = sieveAllNonPrimes(numToPrintAllPrimes)
    for i in range(1, len(primeArr)):
        if (primeArr[i] == 0):
            print(i+1)
        else:
            continue

def verifyPrime(numToVerify):
    primeArr = sieveAllNonPrimes(numToVerify)
    if(primeArr[numToVerify-1] == 0):
        print(str(numToVerify)  + " is prime")
    else:
        print(str(numToVerify)  + " is not prime")

def sieveAllNonPrimes(numToVerify):
    if(numToVerify>1):
        arr = [0] * numToVerify
        sqrtNum = int(math.sqrt(numToVerify))
        for curNum in range(2, sqrtNum):
            for multipleOfCurNum in range(curNum*curNum, numToVerify+1, curNum):
                arr[multipleOfCurNum-1] = 1
        return arr


    else:
        exitOnError("Something went wrong in getPrimeArray...")


def main():
    print("Executing Sieve of Eratosthenes")
    inputNum = int(input("Do you want to\n1.Print all numbers below a number?\n2. Do you want to find whether a number is prime\nEnter your choice[1-2]: "))
    if (inputNum>0 and inputNum<3):
        msgToDisplay = ""

        if(inputNum == 1):
            msgToDisplay = "Enter the number under which you want to print all primes [0-*]: "
        elif(inputNum == 2):
            msgToDisplay = "Enter the number which you find whether it is a prime [0-*]: "

        numToCheckPrimes = int(input(msgToDisplay))
        if(numToCheckPrimes >=0):
            if(inputNum == 1):
                printAllPrimes(numToCheckPrimes)
            else:
                verifyPrime(numToCheckPrimes)
        else:
            exitOnError("The input doesn't make sense. Exiting..")
    else:
        exitOnError("The input doesn't make sense. Exiting..")


if __name__ == '__main__':
    main()
