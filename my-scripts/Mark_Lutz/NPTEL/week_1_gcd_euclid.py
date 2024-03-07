#!/usr/bin/python3.4

def gcd_euclid(m,n):
    
    if(m < n):
        (m,n) = (n,m)

    while(m%n != 0):
        (m,n) = (n,m%n)

    return(n)

print(gcd_euclid(1212,4545))
        
