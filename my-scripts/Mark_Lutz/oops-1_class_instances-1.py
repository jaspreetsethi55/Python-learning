#!/usr/bin/pyhton3.4

'''
Classes allow us to logically group our data and functions, in way that is easy
to re-use and also easy to build upon if needed. 

In short, Class is a blueprint to create instances. We can apply attributes and
methods to those instances.

When we say data and functions that are associated with specific class, we call
those attributes and methods, that’s object-oriented terminology.
data -> attributes
functions -> methods

Method is a function that is associated with a class.
'''

class employee:
  pass

emp1 = employee()
emp2 = employee()

#'emp1' and 'emp2' are instances of class 'employee'

print(emp1) #<__main__.employee object at 0x7f276028b7f0>
print(emp2) #<__main__.employee object at 0x7f276028b828>

