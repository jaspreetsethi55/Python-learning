#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):  
    for rot in range(k):
        a = [a[-1]] + a[:-1]
    return [ a[i] for i in queries]
'''
# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    res = [None] * len(a)

    for rot in range(0,k):
        for i in range(len(a)):
            if(i == (len(a)-1)):
                res[0] = a[i]
            else:
                res[i+1] = a[i]
        a = list(res)

    return [ res[i] for i in queries]
''' 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()
    n,k,q = int(nkq[0]), int(nkq[1]), int(nkq[2]) 
   
    a = list(map(int, input().rstrip().split()))

    queries = []

    for i in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

