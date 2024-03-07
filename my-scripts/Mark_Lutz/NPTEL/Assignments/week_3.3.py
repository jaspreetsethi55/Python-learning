#!/usr/bin/python3.4

'''
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> transpose([[1,4,9]])
[[1], [4], [9]]

>>> transpose([[1,3,5],[2,4,6]])
[[1, 2], [3, 4], [5, 6]]

>>> transpose([[1,1,1],[2,2,2],[3,3,3]])
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

'''

def transpose(l):
    if not l:
        return []
    return [ [row[col] for row in l] for col in range(len(l[0])) ] 

    '''
    nl = []
    for col in range(len(l[0])):
        nl.append([row[col] for row in l])
            
    return nl
    '''

print(transpose([[1,4,3]]))
