def main():
    x = 0

    # define a while loop
    while (x<5):
        print(x)
        x += 1

    # define a for loop

    # An array of values
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for x in range(5, 10, 5):
        print(x)
    for x in range(6, 10):
        print(x)

    # for loop to iterate through a range of numbers
    for x in range(10, 100):
        # break the for
        if(x == 18):
            break
        # continue or skip the iteration
        if (x % 2 == 0):
            continue
        print(x)

    # for loop to iterate through an array
    for day in days:
        print (day)

    # for loop to iterate through a collection
    for index, day in enumerate(days):
        print (index, day)

if __name__ == "__main__":
    main()
