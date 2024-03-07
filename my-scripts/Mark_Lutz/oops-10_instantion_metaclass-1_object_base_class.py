############object base class in Python3#############
'''
In Python3, all classes implicitly inherit from the built-in object base class. The object class provides some common methods, such as __init__, __str__, and __new__, that can be overridden by the child class. Consider the code below, for example:
'''

class Human:
    pass

'''
In the above code, the Human class does not define any attributes or methods. However, by default, the Human class inherits the object base class and as a result it has all the attributes and methods defined by the object base class. We can check all the attributes and the methods inherited or defined by the Human class using the dir function.
'''

#the dir function returns a list of all the attributes and methods defined on any Python object.

print(dir(Human))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '
__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__st
r__', '__subclasshook__', '__weakref__']
'''

'''
The "dir" function's output shows that the Human class has lots of methods and attributes, most of which are available to the Human class from the object base class. 
Python provides a __bases__ attribute on each class that can be used to obtain a list of classes the given class inherits.
'''
#The __bases__ property of the class contains a list of all the base classes that the given class inherits.

print(Human.__bases__)
#Output: (<class 'object'>,)

'''
The above output shows that the Human class has object as a base class. We can also look at the attributes and methods defined by the object class using the dir function.

dir(object)

# Output:
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__']
'''

'''
The above definition of the Human class is equivalent to the following code; here, we are explicitly inheriting the object base class. Although you can explicitly inherit the object base class, it's not required!
'''

class Human(object):
    pass

'''
"object" base class provides __init__ and __new__ methods that are used for creating and initializing objects of a class. We will discuss __init__ and __new__ in detail in the latter part of the tutorial.


object
^
|
|
Human

'''


