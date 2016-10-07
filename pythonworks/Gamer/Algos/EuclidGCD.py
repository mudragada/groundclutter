__author__ = 'Krishna Mudragada'

import logging
class EuclidGCD:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.getLogger().setLevel(logging.INFO)
        logging.info("Initializing EuclidGCD..")
        self.numberList = []
    def addToList(self, number ):
        self.numberList.append(number)
    def printList(self):
        logging.info('\t'.join(map(str, self.numberList)))
    def gcd(self, x, y):
        while x>0:
            logging.debug("IN the while loop x= " + str(x) + " y = " +str(y))
            if(x<y):
                t=x
                x=y
                y=t
            x = x % y
        return y
    def gcdOfList(self):
        return str(reduce(self.gcd,self.numberList))

if __name__ == "__main__":
    gcdObject = EuclidGCD()
    while True:
        number_input = raw_input("Enter number for calculating GCD:")
        if (number_input == ''):
            logging.info("End of input")
            break
        if(not number_input.isdigit()):
            logging.error("Enter a valid number")
            continue
        gcdObject.addToList(int(number_input))
    gcdObject.printList()
    logging.info("GCD of numbers is " + gcdObject.gcdOfList())
