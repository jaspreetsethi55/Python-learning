#!/usr/bin/python3.4

##Limitations:
    #works only on sorted sequence
    #works only on arrays(and not on list(linked-list)) because for only arrays we can get any array[i] in constant time

def binary_search(seq,value,start,end):
    if(end - start <= 0):  ##T(0) = 1
        return 'Not Found'

    mid = (end-start)//2) ##Integer division
    
    if(value == seq[mid]):
        return seq[mid]
    elif(value < seq[mid]): ##if value to be searched is left to mid value
        end = mid
        binary_search = (seq,value,start,end)
    elif(value > seq[mid]): ##if value to be searched is right to mid value
        start = mid + 1
        binary_search = (seq,value,start,end)


seq = [3,4,5,9,11,45,67,89,101,104,108,110,180,280,300,301]
print(binary_search(seq,89,0,len(seq)-1))

'''
Complexity:
As we are dividing seq by half to search(as we are taking mid point)
##Always consider worst case while calulating complexity
#T(0) = 1 i.e. can't find if no elements  left butu that will also take one step/iteration

T(n) = 1 + T(n/2) ##This is recursion
     = 1 + 1 + T(n/4) or 1 + 1 + T(n/2-to-the-power-2)
     = 1 + 1 + ..... + T(n/k) or 1 + 1 + T(n/2-to-the-power-k)
     = 1 + 1 + ..... + T(n/2-to-the-power-log(n))
     = Olog(n)

'''



def binary_search_without_recursion(seq,value):
    start, end = 0, len(seq)-1

    while start < end:
        mid = (start+end)//2

        if value = seq[mid]:
            return mid
        elif value < seq[mid]:
            end = mid
        elif value > seq[mid]:
            start = mid +1
    return -1
    
