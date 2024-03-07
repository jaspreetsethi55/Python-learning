#!/usr/bni/python3.4

print("Am in tmp/jsethi/python/Mark_Lutz/Modules/my_module.py")

var = 'This is test variable in my_module'

def find_index(l,val):
    for index,value in enumerate(l):
        if(val == value):
            return index

    return -1
