#!/usr/bin/env python3

import sys

prevState = None
prevCity = None
stateSum = 0
citySum = 0
line1 = 0

for line in sys.stdin:
    line1 = 1
    line = line.strip().split(",")
    city = line[1].strip()
    state = line[0].strip()

    if(state == prevState):
        if(prevCity == None):
            citySum = 1
            stateSum = stateSum + 1
            prevCity = city
        elif(city == prevCity):
            citySum = citySum + 1
            stateSum = stateSum + 1
        else:
            print(prevCity, citySum)
            citySum = 1
            stateSum = stateSum + 1
            prevCity = city
    elif(prevState == None):
        print(state)
        citySum = citySum + 1
        prevCity = city
        stateSum = 1
        prevState = state
    else:
        print(prevCity, citySum)
        print(prevState, stateSum)
        print(state)
        citySum = 1
        prevCity = city
        stateSum = 1
        prevState = state

if line1:
    print(prevCity, citySum)
    print(prevState, stateSum)
