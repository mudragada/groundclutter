
def main():

    ## Open file in a write(w) and create if not present (*) mode
    f = open("fileops.txt", "a+")
    ## write lines to the file
    for i in range(10):
        f.write("this is line " + str(i) + "\r\n")
    ## close the file
    f.close()
    f = open("fileops.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        print(type(contents))
if __name__ == "__main__":
    main()
