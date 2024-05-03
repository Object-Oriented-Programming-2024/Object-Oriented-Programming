#Import the os module helps interact with the operating system
import os
#Opening the batch file
file = open('startup.bat', mode='r')
#Reading the batch file one line at a time
line=file.readline()
while line:
 # Run each instruction
 exit_code = os.system(line)
 #Reading the next line in the batch file
 line=file.readline()
