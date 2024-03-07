#!/usr/bin/python3.4

'''
A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

>>> valley([3,2,1,2,3])
True

>>> valley([3,2,1])
False

>>> valley([3,3,2,1,2])
False
'''

def valley(l):
    if(len(l) < 3):
        return False

    if(l[0] < l[1]):
        return False

    index = 0
    for i in range(0,len(l)-1):
        if(l[i] < l[i+1]): 
            index = i
            break
        elif(l[i] == l[i+1]):
            return False
    else:
        return False

    for i in range(index,len(l)-1):
        if(l[i] >= l[i+1]):
            return False
    return True


print(valley([3,2,3,4]))
print(valley([3,2,3]))
print(valley([3,2,3,3]))
print(valley([3,2,1,2,3]))
print(valley([17,2,1,2,9]))
