import os
import sys
from datetime import datetime

def main():
    roomsPath = '/Users/sureshvunnam/Desktop/rooms.txt'
    inputPath = '/Users/sureshvunnam/Desktop/inputData.txt'
    inputLines, roomsData = openFiles(roomsPath, inputPath)
    availableRooms, size, startTime, endTime, teamFloor = parseInputFiles(inputLines, roomsData)
    vacantRooms = findNearestRoom(availableRooms, size, startTime, endTime)
    closest(vacantRooms, teamFloor)

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
    startTime = inputList[2]
    endTime = inputList[3]
    size = int(inputList[0])
    floor = inputList[1]
    return inputRooms, size, startTime, endTime, floor


#print(roomsData)
# Find nearest meeting room
def findNearestRoom(roomsData, size, startTime, endTime):
    availableRooms = []
    for room in roomsData:
        i=2
        if(int(room[1]) >= size):
            while(i < len(room)):
                if(room[i]==startTime and room[i+1]==endTime):
                    availableRooms.append(room[0])
                i=i+2
    return availableRooms

def closest(availableRooms, floor): 
    if(len(availableRooms) == 0):
        print("No rooms available")
    else:
        print(min(availableRooms, key=lambda x:abs(float(x)-float(floor))))

if '_name_' == "_main_":
    main()
