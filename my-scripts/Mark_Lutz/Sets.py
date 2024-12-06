###########Sets
'''
A set is a collection of unique data, meaning that elements within a set cannot be duplicated. Though we can add duplicate items but they will be automatically removed when storing so we will never get duplicate items when processing/printing sets. 
In Python, we create sets by placing all the elements inside curly braces {}, separated by commas.

A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

Some Set characteristics:
1. We can never access set elements via indexing or slicing.
2. Sets are mutable, i.e. we can add/delete/modify set elements via using function. E.g. s.add(5)
'''

s = {1,2,8,5,12,7}
print(s) #{1, 2, 5, 7, 8, 12} #will always return sorted set by default

#Mixed mutable data type set 
s = {(1,3,2),"a","z","b",4,1} 
print(s) #{1, 4, (1, 3, 2), 'a', 'z', 'b'}  #Please note that nested tuple inside set is not sorted

#Mixed immutable data type set -- not allowed - will give error
#s = {[1,3,2],"a","z","b",4,1}  #Will give error "TypeError: unhashable type: 'list'"

#######Creating empty set
'''
Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
To make a set without any elements, we use the set() function without any argument.
'''
empty_set = set()
print('Data type of empty_set:', type(empty_set)) # <class 'set'>


########Duplicate items
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}


#########Add,Update & delete Set Items in Python
numbers = {21, 34, 54, 12}

#add: using add() method
numbers.add(32)
print('Updated Set:', numbers) #{32, 34, 12, 21, 54}

#update: update() method is used to update the set with items other collection types (lists, tuples, sets, etc).
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies) #{'google', 'apple', 'Lacoste', 'Ralph Lauren'}

#delete: using discard() method to remove the specified element from a set
languages = {'Swift', 'Java', 'Python'}
removedValue = languages.discard('Java') #languages = {'Python', 'Swift'}

###########Built-in Functions with Set
'''
Here are some of the popular built-in functions that allow us to perform different operations on a set.
Function	Description
all()	Returns True if all elements of the set are true (or if the set is empty).
any()	Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	Returns the length (the number of items) in the set.
max()	Returns the largest item in the set.
min()	Returns the smallest item in the set.
sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	Returns the sum of all elements in the set.
'''

###########Python Set Operations
'''
Python Set provides different built-in methods to perform mathematical set operations like:
    union
    intersection
    subtraction
    symmetric difference.
'''

#Union of Two Sets - We use the | operator or the union() method to perform the set union operation
#The union of two sets A and B includes all the elements of sets A and B.
#Note: A|B and union() is equivalent to A ∪ B set operation.
A = {1, 3, 5}
B = {0, 2, 4}
print('Union using |:', A | B) #{0, 1, 2, 3, 4, 5}
print('Union using union():', A.union(B)) #{0, 1, 2, 3, 4, 5}

#Set Intersection - The intersection of two sets A and B include the common elements between set A and B.
#In Python, we use the & operator or the intersection() method to perform the set intersection operation.
#Note: A&B and intersection() is equivalent to A ∩ B set operation.
A = {1, 3, 5}
B = {1, 2, 3}
print('Intersection using &:', A & B) #{1, 3}
print('Intersection using intersection():', A.intersection(B)) #{1, 3}

#Difference between Two Sets - The difference between two sets A and B include elements of set A that are not present on set B.
#We use the - operator or the difference() method to perform the difference between two sets.
#Note: A - B and A.difference(B) is equivalent to A - B set operation.
A = {2, 3, 5}
B = {1, 2, 6}
print('Difference using &:', A - B) #{3, 5}
print('Difference using difference():', A.difference(B)) #{3, 5}

print('Difference using &:', B - A) #{1, 6}
print('Difference using difference():', B.difference(A)) #{1, 6}

#Set Symmetric Difference - The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
#In Python, we use the ^ operator or the symmetric_difference() method to perform symmetric differences between two sets
A = {2, 3, 5}
B = {1, 2, 6}

print('using ^:', A ^ B) #{1, 3, 5, 6}
print('using symmetric_difference():', A.symmetric_difference(B)) #{1, 3, 5, 6}

#Check if two sets are equal - We can use the == operator to check whether two sets are equal or not


#################################Other Python Set Methods
'''
There are many set methods, some of which we have already used above. Here is a list of all the methods that are available with the set objects:

Method	Description
add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others
'''

#########set pop vs remove vs discard
#Use pop() when you want to remove and use an element from the set, but you don't care which element it is. E.g. s.pop() - will delete any element from set and return it. returns error if set is empty.
#Use remove() when you want to remove a specific element from the set. E.g. s.remove(5) - Raise keyerror if 5 is not there in set s
#If you need to remove an element and you're not sure if it exists, consider using discard() instead of remove(). discard() will not raise an error if the element doesn't exist.

s = {12,1,5,6,3,8}
s.pop() #1
s.pop() #3

s.remove(5)
#s.remove(14) #will return keyerror because 14 is not there in set 

s.discard(6)
s.discard(14) #does nothing as 14 is not there in set s but don't give any error
