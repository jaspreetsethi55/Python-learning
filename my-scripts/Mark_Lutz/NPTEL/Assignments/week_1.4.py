#!/usr/bin/python3.4
import sys

def f(m):
    if m == 0:
        return 0
    else:
        return(m+f(m-1)) # The function terminates for non-negative n with f(n) = factorial of n

print(f(int(sys.argv[1])))
