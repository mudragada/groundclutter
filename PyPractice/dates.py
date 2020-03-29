from datetime import *

def main():
    today = date.today()
    print ("Today's date is ",  today)

    print ("Todays' weekday is ", today.weekday())
    print ("Today's date components ", today.month, today.year)

    now = datetime.now()
## Date Formatting ##
## %y/Y - Year, %a/A - weekday,
    print(now.strftime("%y, %Y, %a, %A, %b, %B, %c, %C, %d, %D, %e, %e, %E, %f, %F, %g, %G, %h, %H"))
    print(now.strftime("DateTime: %c"))
    print(now.strftime("Date: %x"))
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("Current time: %H:%M:%S %p"))

if __name__ == "__main__":
    main()
