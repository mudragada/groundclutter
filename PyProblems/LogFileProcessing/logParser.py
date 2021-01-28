"""
1. Parse from a log file.
2. Extract method, request, status from each line
3. write them to a  CSV
"""

from os import path
import csv

def main():
    print ("I am in main")
    inputFileName = input("Enter the filename:  ")
    if(path.exists(inputFileName)):
        parseLog(inputFileName)
    else:
        print("Enter a valid filename")


def parseLog(inputFile):
    csv_file = "results.csv"
    csv_columns = ['method', 'path', 'status']
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            with open(inputFile, 'r') as logfile:
                lines = logfile.readlines()
                for line in lines:
                    kvDict = {}
                    strings = line.split(" ")
                    for stringer in strings:
                        if("=" in stringer):
                            stringKVList = stringer.split("=")
                            if((stringKVList[0] == 'method' or stringKVList[0] == 'path' or stringKVList[0] == 'status') and stringKVList[1]):
                                kvDict[stringKVList[0]] = stringKVList[1]
                    print(kvDict)
                    writer.writerow(kvDict)
    except IOError:
        print("IO Error")

if __name__ == '__main__':
    main()
