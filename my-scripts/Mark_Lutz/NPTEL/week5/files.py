#!/usr/bin/python3.4

for line in open('file.txt'): #best way to read file. Gives one line at a time
    print("Line:",line)
else:
    print("File has ended.") #Simple way to read end of file


'''
Line: This is line1

Line: Line2 starts here

Line: Hey! this is line3

'''



for line in open('file.txt').read(): #read gives one character at a time
    print("Line:",line)
    if(line == ""): #For recognizing "End of file" . read() and readline() returns empty string "" on eof
       print("File has ended.")

'''
Line: T
Line: h
Line: i
Line: s
Line:
Line: i
Line: s
Line:
Line: l
Line: i
Line: n
Line: e
Line: 1
Line:

Line: L
Line: i
Line: n
...
...
Line:
'''


for line in open('file.txt').readline(): #Gives one character at a time for just first line. don't process other lines
    print("Line:",line)

for line in open('file.txt').readlines(): #Gives one line at a time
    print("Line:",line)
