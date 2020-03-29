def main():
    inputArray = [-23, 4, -3, 8, -12]
    print("Max Adjacent element product is " + str(adjacentElementsProduct(inputArray)))

def adjacentElementsProduct(inputArray):
    maxProduct = -1000000
    for i in range(len(inputArray)):
        if(inputArray[i] !=None and inputArray[i-1] !=None and i!=0):
            product = inputArray[i] * inputArray[i-1]
            print (product)
            if (product > maxProduct):
                maxProduct = product
        else:
            continue
    return maxProduct

if __name__ == '__main__':
    main()
