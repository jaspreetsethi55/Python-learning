'''
There are two types of errors in python:
1. syntax error
2. Exception
'''

############Syntax Error############
#The arrow(^) indicates where the parser ran into the syntax error. In this example, there was one bracket too many

#print(0/0)) 
'''
File "exceptions_1_raise-assert.py", line 7
  print(0/0))
            ^
SyntaxError: invalid syntax
'''

##########Exception error############
#This time, you ran into an exception error. This type of error occurs whenever syntactically correct Python code results in an error. The last line of the message indicated what type of exception error you ran into.
#print(0/0)
'''
Traceback (most recent call last):
  File "exceptions_1_raise-assert.py", line 19, in <module>
      print(0/0)
ZeroDivisionError: division by zero
'''


#########Raise --   Raising an exception at any time -- Self defined exceptions#############
##Syntax - raise Exception(message)

#Raise an exception and end the program(similar to die in perl)
#We can use raise to throw an exception if a condition occurs. The statement can be complemented with a custom exception.
#The program comes to a halt and displays our exception to screen, offering clues about what went wrong.

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
'''
Traceback (most recent call last):
  File "exceptions_1_raise-assert.py", line 32, in <module>
      raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
Exception: x should not exceed 5. The value of x was: 10
'''


#####Assert - The AssertionError Exception Raise an exception if condition is false #########
##Syntax:  assert (condition-true), exception-message
#Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We assert that a certain condition is met.
#If this condition turns out to be True: then that is excellent! The program can continue. 
#If the condition turns out to be False: you can have the program throw an 'AssertionError' exception.

import sys
assert ('linux' in sys.platform),"This code runs on Linux only."

#If you run this code on a Linux machine, the assertion passes. If you were to run this code on a Windows machine, the outcome of the assertion would be False and the result would be the following:
'''
Traceback (most recent call last):
  File "exceptions_1_raise-assert.py", line 56, in <module>
      assert (linux in sys.platform),"This code runs on Linux only."
AssertionError: name 'linux' is not defined
'''

