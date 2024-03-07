#!/usr/bin/python3.4

'''
Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

>>> sumprimes([3,3,1,13])
19
>>> sumprimes([2,4,6,9,11])
13
>>> sumprimes([-3,1,6])
0

'''
import sys

def factors(n):
    factor_list = []
    for i in range(1,n+1):
        if(n%i == 0):
            factor_list.append(i)
    return factor_list


def is_prime(n):
    if(n == 1):
        return True

    factor_list = factors(n)

    if(factor_list == [1,n]):
        return True
    else:
        return False


def sumprimes(l):
    sumprime = 0

    for i in l:
        if(is_prime(i)):
            sumprime += i

    return sumprime

print(sumprimes([1,2,3,6,8,9,1,-1]))
