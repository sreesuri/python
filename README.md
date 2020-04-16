# python

Pre-requisite - Install python 2.7 

Input text files: 
inputData.txt 
rooms.txt 

Coding in Python - Attached basic functionality and extra credit py files 

Conference room scheduling:

As a basic functionality, I took the input of team size, floor and required meeting start and end times. I looped over the available meeting rooms and times file to find the matching start and end times which will append all the available room IDs into a list and wrote a function to find the nearest room available.
This app will take only one requirement to find a meeting room. So, the input should only be one list of requirements and the format is size, floor, start time, end time.
Longer meeting times wouldn’t affect this functionality in any way because this tries to match the start and end times in the file of the available room and gives the corresponding room numbers.

Added functionality to split meetings across the rooms is working fine. I first looped over the file of the room to find a matching start time, first filtered with size. Once I get the start time and if the end time of the corresponding room is less than the required end time, the start time of the function is updated with the end time of the available room with lesser time than the requirement. The function again loops with the updated start time to find a match and the start time is again updated the second found room is less than the time required. This loop occurs multiple times to complete the original start and end times.

Test: I tested with different use cases. The arguments were changed using different scenarios, so I think most of them are covered.
