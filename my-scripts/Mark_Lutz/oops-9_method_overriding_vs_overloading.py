#####Method Overriding####
'''
Method overriding is an example of run time polymorphism. 
In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. 
In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods i.e. A subclass may change the functionality of a Python method in the superclass. It does so by redefining it.
'''

class A:

	def fun1(self):
		print('feature_1 of class A')

	def fun2(self):
		print('feature_2 of class A')


class B(A):

	# Modified function that is
	# already exist in class A
	def fun1(self):
		print('Modified feature_1 of class A by class B')   

	def fun3(self):
		print('feature_3 of class B')


# Create instance
obj = B()

# Call the override function
obj.fun1()

##Output##
'''
Modified feature_1 of class A by class B
'''


########Method Overloading #########not supported in python #####
'''
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.
'''
def add(a,b):
	return a+b

def add(a,b,c):
	return a+b+c

add(2,3)

#Output
'''
Traceback (most recent call last):
File ?<pyshell#8>?, line 1, in <module>
add(2,3)
TypeError: add() missing 1 required positional argument: ?c?
'''

'''
What looks like overloading methods, it is actually that Python keeps only the latest definition of a method you declare to it.

This code doesn?t make a call to the version of add() that takes in two arguments to add. So we find it safe to say Python doesn?t support method overloading.

However, we recently ran into a rather Pythonic way to make this happen. Check this out:
'''

def add(instanceOf,*args):
	if instanceOf=='int':
		result=0
	if instanceOf=='str':
		result=''
	for i in args:
		result+=i
	return result


add('int',3,4,5)
##5
