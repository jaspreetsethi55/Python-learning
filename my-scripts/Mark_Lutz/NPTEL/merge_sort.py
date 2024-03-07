#!/usr/bin/python3.4

#this will merge 2 sorted lists
def merge(list1,list2):
    
    (final_list,m,n) = ([],len(list1),len(list2)) 
    (i,j) = (0,0) 

    #list1 ranges from i to m
    #list2 ranges from j to n

    while(i+j < m+n):
        if(i == m): #if list1 is empty
            final_list.append(list2[j])
            j = j+1
        elif(j == n): #if list2 is empty
            final_list.append(list1[i])
            i = i+1
        elif(list1[i] <= list2[j]): 
            final_list.append(list1[i])
            i = i+1
        elif(list1[i] > list2[j]):
            final_list.append(list2[j])
            j = j+1
    return final_list

def merge_sort(seq,l,r):
    
    if(r-l <= 1):
        return(seq[l:r])

    if(r-l > 1):
        mid = (r+l)//2
        left = merge_sort(seq,l,mid)
        right = merge_sort(seq,mid,r)

        return(merge(left,right))

my_list = [1,2,5,9,14,2,5,7,9,15]
print(merge_sort(my_list,0,len(my_list)))
