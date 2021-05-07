def fizzBuzz(n):
    for i in range(1,n+1):
        divThree = False
        divFive = False
        if(i%3==0):
            divThree = True
        if (i%5==0):
            divFive = True

        if(divThree and divFive):
            print("FizzBuzz")
        elif(divThree and not divFive):
            print("Fizz")
        elif(not divThree and divFive):
            print("Buzz")
        else:
            print(i)

    # Write your code here

if __name__ == '__main__':
    n = 15

    fizzBuzz(n)
