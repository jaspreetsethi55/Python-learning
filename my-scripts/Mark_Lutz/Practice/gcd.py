#!/usr/bin/python3.4

def gcd(m,n):
    if(m < n):
        m,n = n,m

    for i in range(n,0,-1):
        if n % i == 0 and m % i == 0:
            return i

print(gcd(100000,25000))
