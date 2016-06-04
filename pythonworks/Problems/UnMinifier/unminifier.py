import sys
import os
import io
from Constants import JSConstants
from Tokenizer import Tokenizer

class UnMinifier:
    constants = JSConstants()

    def __init__(self):
        self.activeKeywords = dict()
        self.tokenizer = Tokenizer()

    def unminify_file(self,filename):
        fileString = ''
        with open(filename, 'r') as fileStream:
            fileString = fileStream.read()

        #1. validate file
        if(self.checkBrackets(fileString) == False):
            return False
        #2. Extract the number of keywords by count
        if(self.xtractKeywordCounts(fileString) < 0):
            return False

        #3. Print the test tokens
        self.tokenizer.tokenize(fileString)

        #Success
        return True

    def checkBrackets(self, fileString):
        try:
            openRounds = fileString.count(self.constants.openRound)
            closeRounds = fileString.count(self.constants.closeRound)

            openCurls = fileString.count(self.constants.openCurl)
            closeCurls = fileString.count(self.constants.closeCurl)

            openSquares = fileString.count(self.constants.openSquare)
            closeSquares = fileString.count(self.constants.closeSquare)

            if(openRounds != closeRounds or openCurls != closeCurls or openSquares != closeSquares):
                raise
            else:
                print ("The brackets are good..")
        except Exception as ex:
            print ("Error:: your file misses either a ( or { or } or ), Why don't you check it??")
            return False
        #Success
        return True

    def xtractKeywordCounts(self,fileString):
        # find the number of occurrences in filestring
        try:
            for keyword in self.constants.keywordDictionary.keys():
                if(fileString.count(keyword) > 0 ):
                    self.activeKeywords.update({keyword: fileString.count(keyword)})
        except Exception as ex:
            print ("Error:: Issue with reading form fileString variable")
            return -1
        #Success
        return len(self.activeKeywords.keys())

def main():
    unminifierObj = UnMinifier()
    try:
        args = sys.argv[1:]
        filename = None
        if (len(args) == 1):
            filename = args[0]
        else:
            print ("Error:: Filename isn't passed")
            raise
            # check if a valid filename
        if filename:
                # check if file exists
            if os.path.isfile(filename):
                if(unminifierObj.unminify_file(filename)== True):
                    print ("Success:: file unminified successfully")
                else:
                    print ("Error:: UnMinifier.unminify_file failed")
                    raise
            else:
                print ("Error:: Unable to find the file to unminify. Pls check")
                raise
        else:
            print ("Error:: Filename is not present")
            raise
    except Exception as ex:
        print ("Exiting main")
