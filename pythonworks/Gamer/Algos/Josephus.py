__author__ = 'Krishna Mudragada'

import logging

class Josephus:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.getLogger().setLevel(logging.INFO)

    def sequenceDeaths(self, problemSize, stepSize):
        if problemSize < 2:
            logging.error("Problemsize is less than 2")
            return
        sequenceOfDeath = []
        problemList = range(1, problemSize+1)
        index=0
        while problemList:
            index = (index + (stepSize)) % len(problemList)
            sequenceOfDeath.append(problemList[index])
            problemList.pop(index)
            logging.info("Removing index " + str(index) + "from the list. Now the Size of list is " + str(len(problemList)))

        logging.info(sequenceOfDeath)

def main():
    josephusObj = Josephus()
    problemSize = raw_input("Enter problemSize:")
    stepSize = raw_input("Enter stepSize:")
    josephusObj.sequenceDeaths(int(problemSize), int(stepSize))

if __name__ == "__main__":
    main()