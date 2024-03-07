#!/usr/bin/python3.4

def h(m,n):
    ans = 0
    while (m >= n):
        (ans,m) = (ans+1,m-n)
    return(ans)

print(h(231,8)) #28

