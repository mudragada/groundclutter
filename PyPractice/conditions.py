def main():
    x, y = 10, 1000

    #conditional statement for if, elif, else
    if (x < y):
        printstr = "X is less than Y"
    elif(x > y):
        printstr = "X is greater than Y"
    else:
        printstr = "X and Y are equal"
    return printstr

if __name__ == "__main__":
    print(main())
