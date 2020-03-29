from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print
print(timedelta(days=365, hours=5, minutes = 1))

# print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now

print ("one year from now will be " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument

print ("4 hours and 30 minutes from now will be " + str(now + timedelta(hours=4, minutes=30)))

# calculate the date 1 week ago, formatted as a string

print ("1 week ago from now will be " + str (now - timedelta(weeks=1)))

# How many days until Your birthday

today = date.today()
mybd = date(today.year, 6, 6)
if mybd < today:
    print ("My Birthday already went by %s days ago", str(today-mybd.day))
    mybd = mybd.replace(year = today.year + 1)

time_to_mybd = mybd - today
print("It is ",time_to_mybd.days, " more days to my birthday")
print(type(time_to_mybd))
print(type(mybd))
