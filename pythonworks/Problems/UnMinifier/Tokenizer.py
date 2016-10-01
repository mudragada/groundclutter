__author__ = 'Krishna Mudragada'

from Constants import JSConstants
class Tokenizer:

    def getCharAt(self, inputString, curPos):
        return inputString[curPos]

    def tokenize(self, inputString):
        self.tokenParserPos = 0
        self.tokens = []
        #1. Identify keywords and their positions
        curPos = self.tokenParserPos
        while self.tokenParserPos < len(inputString):
            returnTuple = self.findKeyInSubString(inputString,curPos, self.tokenParserPos, JSConstants.keywordDictionary.keys())
            if(returnTuple[0] > 0):
                print(str(returnTuple[0]) + ":" + returnTuple[1])
            self.tokenParserPos += 1

    def getBestPossibleKeyword(self, possibleKeywords):
        if(len(possibleKeywords) == 1):
            return possibleKeywords[0]
    # Detecting
    def findKeyInSubString(self,inputString,startPos, endPos, keys):
        subString = inputString[startPos:endPos]
        possibleKeywords = list()
        for key in keys:
            if(str(subString).find(key) > 0):
                if(str(inputString[endPos:endPos+1]).isalpha() == False):
                    return (str(subString).find(key), key)
        return (-1,None)


