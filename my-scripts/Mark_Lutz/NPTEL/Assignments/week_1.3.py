#!/usr/bin/python3.4
import sys

def h(n):
    f = 0
    for i in range(1,n+1):
        if(n%i == 0):
            f = f+1
    return(f%2 == 1) #return True whenenver n is a perfect square

print(h(int(sys.argv[1])))
