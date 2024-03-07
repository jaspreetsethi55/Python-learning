#!/usr/bin/python3.4

##variable: In python we do not need to initialze the variable datatype, python does it itself based on values assigned to it.
var = 'Hello World' 
print(var) #Hello World

##Single quote and double quotes are identical in python and treats variables as string
var = "Hello World"
print(var) #Hello World

##Escaping: we can use backslash(/) to escape any special character(E.g. quotes)
var = 'Hello\'s World'
print(var) #Hello's World

#quotes inside quotes
var = "Hello's World"
print(var) #Hello's World

var = 'Hello"s World'
print(var) #Hello"s World

##Multiline string
var = '''Hello"s 
World'''
print(var)
#Hello"s
#World

#multiple comments
'''
This is a 
multiline
comment
'''

##variables are not interpolated(values not assigned) in quotes i.e. everything in quotes is string
var = 'abc'
print("var") #var

##How to use any inbuilt python function/method
'''
1. datatype specific functions/methods i.e. specific to each datatype .E.g. s.lower() will work on strings but not on other datatype(will give error)
    syntax: var.method_name()

2. datatype independent i.e. works for all datatype. E.g. len(var)
'''


###################String Methods#################
##lower
var = "Hello World"
print(var.lower())

##uppercase
print(var.upper())

##length
print(len(var)) #11



#####count#######
#s.count(Substr,[start,end])
#return count of 'substr' in string s, start and end are optional
#If substr not found, then returns 0

print(var.count('l')) #3
print(var.count('Hello')) #1
print(var.count('hello')) #0 because its case sensitive 'hello' is all lowercase

print(var.count('l',3))  ##2  var='Hello World' 


#####Find#######
#s.find(substr,start,end)
#return start index of 'substr' in string s, start and end are optional
#If substr not found, then returns -1
print(var.find('l')) #2 var='Hello World'
print(var.find('l',4,14)) #9
print(var.find('z')) #-1


#####Index#######
#s.index(substr,start,end)
#return start index of 'substr' in string s, start and end are optional
#If substr not found, then returns value-error
print(var)
print(var.index('l')) #2 var='Hello World'
print(var.index('l',4,14)) #9

####rindex and rfind#####
#s.rfind(substr,start,end)
#s.rindex(substr,start,end)
##Same as index and find but returns the highest index instead of starting index


###Startswith and endswith######
##s.startswith(substr,start,end)
##s.endswith(substr,start,end)
#start and end are optional. Returns true or False
print(var.startswith('He')) #True
print(var.startswith('he')) #False


##stripping##
#strip - remove spaces from both side, starting and ending
#lstrip - remove spaces from starting(left side)
#rstrip - remove spaces from endinf(right side)

var = '     :Hello     world :   '
print(var.strip()) #:Hello     world :
print(',' + var.lstrip() + ',') #,:Hello     world :   ,
print(var.rstrip()) #     :Hello     world :

#######Index -- starts from 0
#######Indexing -- str[start:end] - give all element from start to end-1 i.e. not including end
var = "Hello World"
first_char = var[0]
print(first_char) #H

#print(var[11]) #IndexError: string index out of range

last_char = var[-1]
print(last_char) #d

last_index = len(var)-1
last_char2 = var[last_index]
print(last_char2) #d

var_substring = var[6:11]
print(var_substring) #World

var_substring2 = var[6:] 
print(var_substring2) #World
