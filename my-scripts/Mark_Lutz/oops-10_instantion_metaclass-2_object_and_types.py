##########objects and types in Python################
'''
Python is an object-oriented programming language. Everything in Python is an object or an instance. Classes, functions, and even simple data types, such as integer and float, are also objects of some class in Python. Each object has a class from which it is instantiated. To get the class or the type of object, Python provides us with the type function and __class__ property defined on the object itself.

let's understand the type function with the help of simple data types, such as int and float.
'''
#simple integer data type
a = 9

# The type of a is int (i.e., a is an object of class int)
type(a)    # Output: <class 'int'>

# The type of b is float (i.e., b is an object of the class float)
b = 9.0
type(b)   # Output: <class 'float'>

'''
Unlike other languages, in Python, 9 is an object of class int, and it is referred by the variable a. Similarly, 9.0 is an object of class float and is referred by the variable b.
'''

##"Type" is used to find the type or class of an object. It accepts an object whose type we want to find out as the first argument and returns the type or class of that object.

'''
We can also use the __class__ property of the object to find the type or class of the object.
'''

##"__class__" is an attribute on the object that refers to the class from which the object was created.

a.__class__   # Output: <class 'int'>
b.__class__   # Output: <class 'float'>

'''
After simple data types, let's now understand the type function and __class__ attribute with the help of a user-defined class, Human. Consider the Human class defined below:
'''

# Human class definition
class Human:
    pass

# Creating a Human object
human_obj = Human()

'''
Above code creates an instance human_obj of the Human class. We can find out the class (or type of human_obj) from which human_obj was created using either the type function or the __class__ property of the human_obj object.
'''

# human_obj is of type Human
type(human_obj)     # Output: <class '__main__.Human'>

human_obj.__class__ # Output: <class '__main__.Human'>



