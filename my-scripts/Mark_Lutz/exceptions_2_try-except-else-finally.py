#####try/except#########
#######################
'''
**A try clause is executed up until the point where the first exception is encountered.

**Inside the except clause, or the exception handler, you determine how the program responds to the exception.

**You can anticipate multiple exceptions and differentiate how the program should respond to them.

**Avoid using bare except clauses.
'''

#The try and except block in Python is used to catch and handle exceptions.
'''
try: Python executes code following the try statement as a “normal” part of the program. 
except: The code that follows the except statement is the program’s response to any exceptions in the preceding try clause. except clause determines how your program responds to exceptions.
'''
import sys

def windows_interaction():
    assert ('win32' in sys.platform), "Function can only run on Windows system."
    print('Doing something.')

#The windows_interaction() can only run on a windows system. The assert in this function will throw an AssertionError exception if you call it on an operating system other then windows.

try:
    windows_interaction()
except: #This will be executed, since this is linux system
    print('Windows Function was not executed')

'''Output: Windows Function was not executed'''

######Catching Errors with except#####
######################################
'''In Above code, What you did not get to see was the type of error that was thrown as a result of the function call. In order to see exactly what went wrong, you would need to catch the error that the function threw.

The following code is an example where you capture/caught the 'AssertionError' and output that message to screen:
'''
try:
    windows_interaction()
except AssertionError as error: #This will be executed, since this is linux system
    print('Error:',error)
    print('Function windows_interaction() was not executed')
'''Output:
Function can only run on Windows system.
Function windows_interaction() was not executed
'''
#The first message is the AssertionError, informing you that the function can only be executed on a Linux machine. The second message tells you which function was not executed.



#######Catching built in exceptions with except#################
##############################################################
try:
    with open('file.log') as file:
        read_date = file.read()
except:
    print("Could not open file.log")
'''Output: Could not open file.log'''

##Warning: Catching Exception hides all errors…even those which are completely unexpected. This is why you should avoid bare except clauses in your Python programs. Instead, you’ll want to refer to specific exception classes you want to catch and handle.

#with open('file.log') as file:
#    read_date = file.read()
'''Output:
Traceback (most recent call last):
  File "exceptions_2_try-except-else-finally.py", line 49, in <module>
      with open('file.log') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'file.log'
'''
#So, we can see that there's big difference between error we print vs default error. So,we should always capture errors by names and instead use it our printed errors as below:
try:
    with open('file.log') as file:
        read_date = file.read()
except FileNotFoundError as error:
    print(error)
    print("Could not open file.log")
'''Output:
[Errno 2] No such file or directory: 'file.log'
Could not open file.log
'''

##Notice that above code doesn't print the complete error(E.g. line num , etc), it only print part of error we captured. E.g. "[Errno 2] No such file or directory: 'file.log'", we can use 'traceback' module to capture complete error

import traceback
import sys

try:
    with open('file.log') as file:
        read_date = file.read()
except FileNotFoundError as error:
    print('TRACEBACK:',traceback.format_exc())  #####This will print complete error even while using try/except i.e. even when using error handling
    print(error)
    print("Could not open file.log")


#############Handling Mutilple exceptions##############
###########################################################
try:
    windows_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Windows windows_interaction() function was not executed')


###########else clause################
#################################
#'else' lets you code sections that should run only when no exceptions are encountered in the try clause.

##############finally clause#############
########################################
#'finally' enables you to execute sections of code that should always run, with or without any previously encountered exceptions

try:
    windows_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        print("Reading File:file.log")
finally:
    print('Cleaning up, irrespective of any exceptions.')

