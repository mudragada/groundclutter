import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("Item exists: " + str(path.exists("./PyPractice/conditions.py")))
    print("isDirectory ./PyPractice/conditions.py: " + str(path.isdir("./PyPractice/conditions.py")))
    print("isDirectory ./PyPractice: " + str(path.isdir("./PyPractice")))
    print("isFile ./PyPractice: " + str(path.isfile("./PyPractice")))
    print("isFile ./PyPractice/conditions.py: " + str(path.isfile("./PyPractice/conditions.py")))

    ## Delete a fileops
    if(path.exists("fileops.txt")):
        os.unlink("fileops.txt")

    ## Get Modification time of a file
    t = datetime.datetime.fromtimestamp(path.getmtime("./PyPractice/functions.py"))
    print (t)

if __name__ == "__main__":
    main()
