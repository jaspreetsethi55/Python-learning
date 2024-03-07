#####
#In general, using 'return' function inside 'try', when 'try' is used within a functioin, will skip the 'else' section
####


l = [1,2,3,4,2]
def get_error():
    assert (1 in l),'Element not fount in list l'

import traceback   

def func_error():
	try:
		get_error()    ##In this case,we are not getting 'error', so 'except' block will not be executed' and 'return' function will also skip 'else' block.
		return 'Am returning'
	except AssertionError as error:
		print(traceback.format_exc())
		print(error)
		print('We have got error in function get_error')
	else:
		print('Function get_error was executed successfully')
	finally:
		print('This is always executed')

print(func_error())

'''
This is always executed

Am returning
'''


def get_error2():
    assert (5 in l),'Element not fount in list l'

def func_error2():
	try:
		get_error2()    ##In this case,we are getting error, so 'except' block will be executed' and finally block and and thus 'return' function will no be executed 
		return 'Am returning'
	except AssertionError as error:
		print(traceback.format_exc())
		print(error)
		print('We have got error in function get_error')
	else:
		print('Function get_error was executed successfully')
	finally:
		print('This is always executed')

print(func_error2())

'''
Traceback (most recent call last):

File "<string>", line 12, in func_error

File "<string>", line 6, in get_error

AssertionError: Element not fount in list l



Element not fount in list l

We have got error in function get_error

This is always executed

'''
