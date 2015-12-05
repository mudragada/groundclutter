import math

def inputSize():x = input('enter the Problem Size');return int(x)
def bitArray(probSize): return ([True for i in range(1,probSize+1)])

## Define a range with custom Step size
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
        
## Print Primes by Sieve method
def printPrimeBySieve(probSize):
    primeArr = bitArray(probSize+1)
    for curNum in range(2,int(math.sqrt(probSize))):
        if(primeArr[curNum]):
            print(str(curNum) + " ")
            for multipleOfCurNum in my_range(curNum*curNum, probSize, curNum):
                primeArr[multipleOfCurNum] = False
    
    for curNum in range (int(math.sqrt(probSize))+1, probSize):
        if(primeArr[curNum]):
            print(str(curNum) + " ")
        

# Print Primes by regular method
def printPrime(probSize):
    for curNum in range(2, probSize+1):
        isPrime = True
        for divisor in range(2, curNum-1):
            if(curNum % divisor == 0):isPrime = False; break
        if (isPrime):
            print(str(curNum) + " ")
def main():
    problemSize = inputSize()
    ## Time Spent
    import time
    start_time_sieve = time.time()
    printPrimeBySieve(problemSize)
    time_taken_for_sieve = time.time() - start_time_sieve

    start_time_regular = time.time()
    printPrime(problemSize)
    time_taken_for_regular = time.time() - start_time_regular
    print("---Sieve in %s seconds --- vs --- Regular in %s seconds" % (time_taken_for_sieve,time_taken_for_regular))

main()