import os
import sys
import unittest
from datetime import datetime as dt
import itertools

# Reading file from local path

def openFiles(roomsPath, inputPath):
    try:
        with open(roomsPath, 'r') as f:
            roomsData = f.read().splitlines()
    except OSError:
        print ("Could not open/read file:" + roomsPath)
        sys.exit()
    try:
        with open(inputPath, 'r') as i:
            inputLines = i.read().splitlines()
    except OSError:
        print ("Could not open/read file:" + inputPath)
        sys.exit()
    return inputLines, roomsData

# Parse input file
def parseInputFiles(inputLines, roomsData):
    inputList = []
    for item in inputLines:
        inputList = item.split(",")
    inputRooms = []
    for item in roomsData:
        i = item.split(",")
        inputRooms.append(i)
    for item in inputRooms:
        for x in item[2:]:
            dt.strptime(x, '%H:%M').time()
    startTime = inputList[2]
    endTime = inputList[3]
    size = int(inputList[0])
    floor = inputList[1]
    return inputRooms, size, startTime, endTime, floor

# Find nearest meeting room 
# * When one room fits requirements*
def findNearestRoom(roomsData, size, startTime, endTime):
    availableRooms = []
    flag = 0
    for room in roomsData:
        i=2
        if(int(room[1]) >= size):
            while(i < len(room)):
                if(room[i]==startTime and room[i+1]==endTime):
                    availableRooms.append(room[0])
                    flag = 1
                    break
                i=i+2
            if(flag == 1): break
    if (len(availableRooms) == 0):
        availableRooms = splitMeetingsAcrossRooms(roomsData, size, startTime, endTime)
    return availableRooms

def printNearestAvailableRoom(availableRooms, floor): 
    for item in availableRooms:
        item = str(item)
    if(len(availableRooms) == 0):
        print("No rooms available")
    if(len(availableRooms) == 1):
        print("Room " + availableRooms[0] + " available")
    else:
        i=0
        while(i <= len(availableRooms)-3):
            print("Time: " + str(availableRooms[i])
            +" "+ "to " + str(availableRooms[i+1])
            +" "+ " Room number: " + str(availableRooms[i+2]) + "\n")
            i=i+3

# When one room is not available, we split across rooms
def splitMeetingsAcrossRooms(roomsData, size, startTime, endTime):
    for item in roomsData:
        for y in range(len(item)-2):
                item[y+2] = dt.strptime(item[y+2], '%H:%M').time()
    startTime = dt.strptime(startTime, '%H:%M').time()
    endTime = dt.strptime(endTime, '%H:%M').time()
    availableRooms = []
    def findMultipleRooms(startTime, endTime):
        originalEndTime = endTime
        # flag when originalEndTime matches with end times found in input data
        flag = 0
        counter = 0
        for item in range(len(roomsData)):
            for room in roomsData:
                # 'i' is the counter to iterate through the items of input file
                i=2
                if(int(room[1]) >= size):
                    while(i < len(room)):
                        if(room[i]==startTime):         
                            if(room[i+1] <= endTime):
                                availableRooms.append(startTime)
                                availableRooms.append(room[i+1])
                                availableRooms.append(room[0])
                                if(availableRooms[-2] == originalEndTime and item == counter):
                                    flag = 1
                                    break
                                else:
                                    startTime = room[i+1]
                                    i=i+2
                                    continue
                            else: continue
                        else:
                            i=i+2
                            continue
                    if(flag == 1): break
                    else:
                        counter=counter+1
                        continue
                    
        return availableRooms
    return findMultipleRooms(startTime, endTime)

def main():
    roomsPath = '/Users/sureshvunnam/Desktop/rooms.txt'
    inputPath = '/Users/sureshvunnam/Desktop/inputData.txt'
    inputLines, roomsData = openFiles(roomsPath, inputPath)
    availableRooms, size, startTime, endTime, teamFloor = parseInputFiles(inputLines, roomsData)
    vacantRooms = findNearestRoom(availableRooms, size, startTime, endTime)
    printNearestAvailableRoom(vacantRooms, teamFloor)

if '_name_' == "_main_":
    main()
