#!/usr/bin/python3.4

'''
Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

>>> intreverse(783)
387
>>> intreverse(242789)
987242
>>> intreverse(3)
3
'''


import sys

def intreverse(n):
    ans = 0
    while(n > 0):
        (rem,n) = (n%10,n//10)
        ans = (ans * 10) + rem
    return(ans)

print(intreverse(int(sys.argv[1])))
