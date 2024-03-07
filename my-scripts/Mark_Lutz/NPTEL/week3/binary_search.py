#!/usr/bin/python3.4

##Binary Search for sorted sequence

def binary_search(seq,v,l,r):
    if((r - l) <= 0):
        return 'slice empty'

    mid = (r+l)//2

    if(v == seq[mid]):
        return mid

    if(v < seq[mid]):
        return (binary_search(seq,v,l,mid))
    else:
        return (binary_search(seq,v,mid+1,r))

seq = [5,6,9,10,34,56,78,90,101,105,202,303,400,506,708]
(v,l,r) = (34,0,len(seq)-1)
(v,l,r) = (506,0,len(seq)-1)
print(binary_search(seq,v,l,r))
