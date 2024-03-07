#!/usr/bin/python3.4

def insertion_sort(seq):

    for slice_end in range(len(seq)):
        pos = slice_end
        while(pos > 0 and seq[pos] < seq[pos-1]):
            seq[pos-1],seq[pos]=seq[pos],seq[pos-1]
            pos = pos -1

    return seq

print(insertion_sort([2,5,1,0,10,34,56]))


'''
complexity: 
T(n) = 1 + 2 + 3 ... + n-1
     = n(n-1)/2
     = O(n-to-the-power-2)
'''
