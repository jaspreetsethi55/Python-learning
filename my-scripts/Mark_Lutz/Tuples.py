#############Tuples:
'''
Python Tuple is a collection of objects separated by commas in round '()' brackets. A tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.
'''

# Note : In case of list, we use squarecbrackets []. 
#Here we use round brackets ()
t = (10, 20, 30)

print(t) #(10, 20, 30)
print(type(t)) #<class 'tuple'>


############Tuples Characteristics:
'''
Like Lists, tuples are ordered and we can access their elements using their index values
We cannot update items to a tuple once it is created.
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created.
IMPORTANT: If a tuple itself contains mutabale datatype(E.g. list) as an element, then we can modify that nutable datatype(E.g. list)
'''

t = (1, 2, 3, 4, 5)

# tuples are indexed
print(t[1]) #2
print(t[4]) #5

# tuples contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t) #(1, 2, 3, 4, 2, 3)

# updating an element
#t[1] = 100 #This will give error "TypeError: 'tuple' object does not support item assignment"
#print(t)

# deleting an element 
#del t[1] #This will give error "TypeError: 'tuple' object doesn't support item deletion"

#updating list inside tuple
#IMPORTANT: If a tuple itself contains mutabale datatype(E.g. list) as an element, then we can modify that nutable datatype(E.g. list)
t = ([1,2,3,5],'a',5)
t[0][1] = 10
print(t) #([1, 10, 3, 5], 'a', 5)



######################Different Ways of Creating a Tuple
#Using round brackets
#Without Brackets
#Tuple Constructor
#Empty Tuple
#Single Element Tuple

#Using Round Brackets
t = ("gfg", "Python")
print(t) #('gfg', 'Python')

#Using Comma Separated
# Creating a tuple without brackets
t = 4, 5, 6
print(t) #Output: (4, 5, 6)

#Using Tuple Constructor
# Creating a tuple using the tuple() constructor
t = tuple([7, 8, 9]) #This actually also converts a list in to Tuple
print(t)  #Output: (7, 8, 9)

#Creating an Empty Tuple
# Creating an empty tuple
t = ()
print(t)  # Output: ()

#Single Element Tuple
# Creating a single-element tuple
t = (10, ) # Comma is important here
print(t)  # Output: (10,)
print(type(t)) #<class 'tuple'>

# What if we do not use comma
t = (10) # This an integer (not a tuple)
print(t) #10
print(type(t)) #<class 'int'>



################Different Operations Related to Tuples
'''
Below are the different operations related to tuples in Python:
Traversing
Concatenation # t = t1 + t2
Nesting # t = (t1, t2)
Repetition # t = ("a",) *3
Slicing 
Deleting # Not allowed, will give error
Finding the length
Multiple Data Types with tuples
Conversion of lists to tuples # t = tuple(["a","b","c"])
Tuples in a Loop
'''
