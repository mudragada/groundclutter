import os
from os import path
import shutil

def main():

    if(path.exists("textfile.txt")):
        src = path.realpath("textfile.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)
        shutil.copystat(src, dst)
        os.rename("textfile.txt", "newtextfile.txt")
    else:
        f = open("textfile.txt", "a+")
        for i in range(10):
            f.write("This is line num: " + str(i) + "\r\n")
        f.close()



if __name__ == "__main__":
    main()
