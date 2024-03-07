#!/usr/bin/python3.4

'''
Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. For instance:

>>> descending([])
True

>>> descending([4,4,3])
True

>>> descending([19,17,18,7])
False
'''

def descending(l):
    for i in range(0,len(l)-1):
        if(l[i] < l[i+1]):
            return False
    return True

print(descending([5,4,3,2,3]))
print(descending([5,4,3,2]))
print(descending([5,4,4,3,2]))
print(descending([]))
