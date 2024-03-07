#!/usr/bin/python3.4

def insertion_sort(l):
    
    for start in range(0,len(l)):
        
        pos = start
        while(pos > 0 and l[pos] < l[pos-1]): ##compare 2 conseutive elements and swap if current leemt is smaller then previous element
            (l[pos-1],l[pos]) = (l[pos], l[pos-1])
            pos = pos - 1
        
    return l

print(insertion_sort([4,2,6,5,9,8,7,1,3]))
