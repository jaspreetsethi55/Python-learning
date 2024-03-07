#!/usr/bin/python3.4

def g(x):
    (q,d) = (1,0)

    while q <= x:
        (q,d) = (q*10,d+1)
    return(d)

print( g(31415927) )  ##8
