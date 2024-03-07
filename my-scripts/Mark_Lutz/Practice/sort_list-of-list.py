#!/usr/bin/python3.4

l = [ [45,56,23],[1,4,5],[0,1,5],[2,1,5] ];

def generic_sort(l):
    for i in range(len(l)):
        if isinstance(i,list):
            l[i] = sorted(l[i])
                
    return sorted(l)

print(generic_sort(l))

l = [ [45,56,23],[1,4,5],[0,1,5],[2,1,5] ];

generic_sorted = sorted(l,key=lambda k : k[0]))
print(generic_sorted)
