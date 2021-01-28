""" If a number is divisible by 4, print "Happy". If a number is divisible by 6, print "Birthday". if an number is divisible by both 4 and 6, print "Happy Birthday"
"""
def main():
    var = input("Enter a number")
    printConditionalText(int(var))

def printConditionalText(var):

    if (var%4 == 0 and var%6 == 0):
        print("Happy Birthday")
    elif (var % 4 == 0):
        print("Happy")
    elif (var % 6 == 0):
        print ("Birthday")
    else:
        print ("Enter a valid number")

if __name__ == "__main__":
    main()
