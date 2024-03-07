'''
#####Inheritance('is a' relationship. Class 'Animal' is a class 'Horse')######
Note: In an inheritance relationship:

##Classes that inherit from another are called derived classes, subclasses, or subtypes.
##Classes from which other classes are derived are called base classes or super classes.
##A derived class is said to derive, inherit, or extend a base class.

This means that when you have a Derived class that inherits from a Base class, you created a relationship where Derived 'is a' specialized version of Base.
Let’s say you have a base class Animal and you derive from it to create a Horse class. The inheritance relationship states that a Horse is an Animal. This means that Horse inherits the interface and implementation of Animal, and Horse objects can be used to replace Animal objects in the application.

This is known as the Liskov substitution principle. The principle states that “in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program”.

######Composition('has a' relationship. Claass 'Horse' has a class 'tail')######
Composition is a concept that models a 'has a' relationship.
It enables creating complex types by combining objects of other types. This means that a class 'Composite' can contain an object of another class 'Component'. This relationship means that a Composite 'has a' Component.

Note: Classes that contain objects of other classes are usually referred to as composites, where classes that are used to create more complex types are referred to as components.

For example, your Horse class can be composed by another object of type Tail. Composition allows you to express that relationship by saying a Horse has a Tail.

Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes. Both Horse and Dog classes can leverage the functionality of Tail through composition without deriving one class from the other.
'''
####################################Overview Of inheritance#####################################
################################################################################################


#########Object Super Class###########
'''Every class you create in Python implicitly derives from class 'object'(The exception to this rule are classes used to indicate errors by raising an exception.)'''

'''When you write Python code using classes, you are using inheritance even if you don’t know you’re using it'''
class MyClass:
    pass

c = MyClass()
print(dir(c))
'''['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']'''

'''Since we have not declared any members in MyClass, so where is the list coming from? Let's see below:'''
o = object()
print(dir(o))
'''['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']'''

#The two lists are nearly identical. There are some additional members in MyClass like __dict__ and __weakref__, but every single member of the object class is also present in MyClass.
#This is because every class you create in Python implicitly derives from class 'object'. You could be more explicit and write class MyClass(object):, but it’s redundant and unnecessary


######Exceptions Are an Exception#######
'''Every class that you create in Python will implicitly derive from object. The exception to this rule are classes used to indicate errors by raising an exception.'''

class MyError:
    pass

#raise MyError()
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException
'''

#We created a new class 'MyError' for indicating type of error and raised an exception using it. An exception is raised but the output states that the exception is of type 'TypeError' not 'MyError' and that all exceptions must derive from 'BaseException'.

#'BaseException' is a base class provided for all error types. To create a new error type, you must derive your class from 'BaseException' or one of its derived classes. The convention in Python is to derive your custom error types from 'Exception', which in turn derives from 'BaseException'.

class MyError(Exception):
    pass
 
raise MyError()
#Now, when we raise 'MyError', the output correctly states the type of error raised i.e. MyError
'''
Traceback (most recent call last):
  File "oops-4_class-inheritance-2.py", line 65, in <module>
      raise MyError()
__main__.MyError
'''

