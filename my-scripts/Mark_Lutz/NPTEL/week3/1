#!/usr/bin/python3.4

def selection_sort(l):

    #l[0,len[l]], l[1,len[l]], ....
    for start in range(0,len(l)):
        
        ##minpos is minimum position of each scan
        minpos = start
        
        for i in range(start,len(l)):
            if(l[i] < l[minpos]):
                minpos = i

        (l[start],l[minpos]) = (l[minpos],l[start])

    return l

print(selection_sort([3,4,5,1,0,6,7,2,4,1,5,8,2,9]))
