#!/usr/bin/python3.4

my_str = 'brown fox is quick brown fox brown'

##using 'find'
occurance1 = my_str.find('brown') #0
occurance2 = my_str.find('brown',5,len(my_str)) #19
occurance3 = my_str.find('cat') # returns -1 i.e. if pattern is not found in str then it returns -1

#using 'index'
occurance1 = my_str.index('brown') #0
occurance2 = my_str.index('brown',5,len(my_str)) #19

try:
    occurance3 = my_str.index('cat') #gives 'ValueError' i.e. if pattern is not found in str then it gives 'ValueError'
except(ValueError):
    print("Substring 'cat' not found")


#replace - doen't chnage the str itself as strimgs are immutable
new_str1 = my_str.replace('brown','black') #replaces all occurances of 'brown' with 'black'
new_str2 = my_str.replace('brown','black',2) #replace only first 2 occurances of 'brown' with 'black'


#formatting strings
my_str = 'hello'
print(my_str.center(25)) #returns new string of length 25 with my_str centered in it
#          hello           

print(my_str.center(25,'-')) #instead of blank spaces, we can give any character to fill those blank spaces 
#----------hello----------

print(my_str.ljust(25))
#hello

print(my_str.ljust(25,'-'))
#hello--------------------

print(my_str.rjust(25))
#                    hello

print(my_str.rjust(25,'-'))
#--------------------hello




