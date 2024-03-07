#Sometimes, its useful to pass arguments to your decorators to make decorators more customizeable.
#For E.g. number of times to execute the decorated function could then be given as an argument.

def decorator_arg(num_times=5):
	def my_decorator(func):
		def wrapper(arg):
			for _ in range(num_times):
				print('Am in decorator wrapper function:{}:{}'.format(_,arg))
			print(arg)
			return func(arg)
		return wrapper
	return my_decorator

####Explaining how each function is called
def func(arg):
	print(arg)
	print('Am in function:{}'.format(arg))

a = decorator_arg(3)
b = a(func)
b('Test')


##How its implemeneted###
@decorator_arg(3)
def func(arg):
	print('Am in function:'.format(arg))

func('Test')





###With a little bit of care, you can also define decorators that can be used both with and without arguments. Most likely, you don?t need this, but it is nice to have the flexibility.
def decorator_arg(_func=None,*,num_times=5):   #1
	def my_decorator(func):
		def wrapper(arg):
			for _ in range(num_times):
				print('Am in decorator wrapper function:{}:{}'.format(_,arg))
			return func(arg)
		return wrapper
	if _func is None:                      #2
		return my_decorator
	else:
		return my_decorator(_func)     #3
'''
1. If 'decorated_arg' has been called without arguments i.e. @decorated_arg, the decorated function will be passed in as _func. 
   If it has been called with arguments @decorated_arg(num_times=3), then _func will be None, and some of the keyword arguments may have been changed from their default values. 
   The * in the argument list means that the remaining arguments can?t be called as positional arguments.
2. In this case, the decorator was called with arguments. Return a decorator function that can read and return a function.
3. In this case, the decorator was called without arguments. Apply the decorator to the function immediately.
'''

#@decorated_arg(3) --- This will give error as * in "def decorator_arg(_func=None,*,num_times=5):" means @decorated_arg can't be called with postional arguments
@decorator_arg(num_times=3)
def func(arg):
	print('Am in function:'.format(arg))

func('Test')

@decorator_arg
def func(arg):
	print('Am in function:'.format(arg))

func('Test')



