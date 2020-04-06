
#Consider a city where the streets are perfectly laid out to form an infinite square grid.
#In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities.
#As a new Uber developer, you are tasked to create an algorithm that does this calculation.
#
#Given user's departure and destination coordinates, each of them located on some street,
# find the length of the shortest route between them assuming that cars can only move along the streets.
# Each street can be represented as a straight line defined by the x = n or y = n formula, where n is an integer.
#
#Example
#
#For departure = [0.4, 1] and destination = [0.9, 3], the output should be
#perfectCity(departure, destination) = 2.7.
#
#0.6 + 2 + 0.1 = 2.7, which is the answer.
#
#Input/Output
#
#[execution time limit] 4 seconds (py3)
#
#[input] array.float departure
#
#An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.
#
#Guaranteed constraints:
#0.0 ≤ departure[i] ≤ 10.0.
#
#[input] array.float destination
#
#An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.
#
#Guaranteed constraints:
#0.0 ≤ destination[i] ≤ 10.0.
#
#[output] float
#
#The shorted distance between two points along the streets.

import math

def main():
    departure = [0.4, 1]
    destination = [0.9, 3]
    print(perfectCity(departure, destination))

    departure = [2.4, 1]
    destination = [5, 7.3]
    print(perfectCity(departure, destination))

    departure = [0, 0.2]
    destination = [7, 0.5]
    print(perfectCity(departure, destination))

    departure = [0.9, 6]
    destination = [1.1, 5]
    print(perfectCity(departure, destination))

    departure = [0, 0.4]
    destination = [1, 0.6]
    print(perfectCity(departure, destination))



def perfectCity(departure, destination):
    print(departure, destination)
    x1 = departure[0]
    x2 = destination[0]
    y1 = departure[1]
    y2 = destination[1]
    xDist = 0
    yDist = 0
    if(int(x1) > int(x2)):
        xDist = x1 - math.floor(x1) + math.ceil(x2) - x2
    elif(int(x1) < int(x2)):
        xDist = math.ceil(x1) - x1 + x2 - math.floor(x2)
    elif(int(x1) == int(x2) and (x1+x2-int(x1)-int(x2)) <=1):
        xDist = x1-math.floor(x1) + x2-math.floor(x2)
    else:
        xDist = math.ceil(x1)-x1 + math.ceil(x2)-x2
    print("X Distance = " + str(xDist))


    if(int(y1) > int(y2)):
        if(isinstance(y1, int)):
            y1x = y1
        else:
            y1x = y1 - math.floor(y1)
        if(isinstance(y2, int)):
            y2x = -y2
        else:
            y2x = math.ceil(y2) - y2
        yDist =  y1x + y2x
    elif(int(y1) < int(y2)):
        if(isinstance(y1, int)):
            y1x = -y1
        else:
            y1x = math.ceil(y1) - y1
        if(isinstance(y2, int)):
            y2x = y2
        else:
            y2x = y2 - math.floor(y2)
        yDist =  y1x + y2x
    elif(int(x1) == int(x2) and (x1+x2-int(x1)-int(x2)) <=1):
        yDist = y1-math.floor(y1) + y2-math.floor(y2)
    else:
        yDist = math.ceil(y1)-y1 + math.ceil(y2)-y2
    print("Y Distance = " + str(yDist))

    return xDist + yDist


if __name__ == '__main__':
    main()
