#!/usr/bin/python3.4

#5,8,3,1,10,4,0

#Step:1 Find min val and exchange it to starting pos
#0,8,3,1,10,4,5

#Step:2 Now start fom 2nd pos(start+1), since starting pos is already min after step-1. Find min value and replace with 2nd pos
#0,1,3,8,10,4,5

#Step:3 Now start fom 3rd pos(start+2), since starting and second pos is already min after step-1 and Step-2. Find min value and replace with 3rd pos
#0,1,3,8,10,4,5

##Repeat/take-forward the above steps.

def selection_sort(seq,start=0):

    if start == len(seq)-1:
        return seq 

    min_pos = start
    for pos in range(start+1,len(seq)):
        if seq[pos] < seq[min_pos]:
            min_pos = pos

    seq[start],seq[min_pos] = seq[min_pos],seq[start]
    start = start + 1

    sorted_seq = selection_sort(seq,start=start)
    return sorted_seq

def selection_sort_without_recursion(seq):
    
    for start in range(len(seq)):
        min_pos = start
        for pos in range(start+1,len(seq)):
            if(seq[pos] < seq[min_pos]):
                min_pos = pos

        seq[start],seq[min_pos]=seq[min_pos],seq[start]

    return seq
    
seq = selection_sort([3,5,8,1,98,56,34,90])
print(seq)
seq = selection_sort_without_recursion([2,5,8,1,98,26,34,90])
print(seq)

'''        
Complexity:
T(n) = n + n-1 + n-2 + ..... 1
     = n(n+1)/2
     = O(n-to-the-power-2)
'''
