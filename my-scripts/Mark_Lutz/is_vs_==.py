'''
== is for value equality. Use it when you would like to know if two objects have the same value.
is is for reference equality. Use it when you would like to know if two references refer to the same object.

is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
'''

>>> a = [1, 2, 3]
>>> b = a
>>> b is a 
True
>>> b == a
True

# Make a new copy of list `a` via the slice operator, 
# and assign it to variable `b`
>>> b = a[:] 
>>> b is a
False
>>> b == a
True
