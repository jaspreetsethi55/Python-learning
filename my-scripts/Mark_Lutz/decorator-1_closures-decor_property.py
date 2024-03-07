#############How decorators work:################
##Decorators work on concept of closures(function within function) and first class objects/functions(i.e. treating functions as any other object i.e. we can pass functions as arguments to other functions, we can return functions, etc)
##Closures allow us to take advantage of first class functions and return an inner functions that has access of variable created in local scope of main(outer) function i.e. provides kind of state retention

##closures
def outer_function(msg):
    message = msg

    def inner_function():
        print(message) ##remembers var local to outer function

    return inner_function ##return inner function object

my_func = outer_function('Hi')
my_func() ##Hi

my_func2 = outer_function('Bye')
my_func2() #Bye

##Closures
def decorator_function(msg):
    def wrapper_function(name):
        print(msg + ' ' + name) ##remembers var local to outer function as well as local to itself

    return wrapper_function ##return inner function object

my_func = decorator_function('Hi')
my_func('Jaspreet') ##Hi Jaspreet

my_func2 = decorator_function('Bye')
my_func2('Bad Habits') #Bye Bad Habits



########What is a Decorator:#########
##Decorator is a function that takes another function as an argument, adds some kind of functionality and then returns another fucntion, all of this without altering the source code of function we passed it.

##Our first Decorator
def decorator_function(org_func):  ##Decorators accepts function as an argument
    def wrapper_function():
        return org_func() ##adds some kind of functionality and then returns another function

    return wrapper_function ##return inner function object

def original_function():
    print("This is original function")

decor_func = decorator_function(original_function)
decor_func() #This is original function




#####Decorating our functions allow us to easily add functionalities to our existing functions by adding that function inside of that wrapper#######
#For example, here without modifying our original_function in any way, we can come inside wrapper and add any kind of code we want, below is same:
def decorator_function(org_func):  ##Decorators accepts function as an argument
    def wrapper_function():
        print("This is new functionlity added to {} without changing it".format(original_function.__name__))
        return org_func() ##adds some kind of functionality and then returns another function

    return wrapper_function ##return inner function object

def original_function():
    print("This is original function")

decor_func = decorator_function(original_function)
decor_func() #This is original function




########decorator property form i.e. @decorator form################
def decorator_function(org_func):  ##Decorators accepts function as an argument
    def wrapper_function():
        print("This is new functionlity added to {} without changing it".format(original_function.__name__))
        return org_func() ##adds some kind of functionality and then returns another function

    return wrapper_function ##return inner function object

@decorator_function ##Now calling original_function will be same as saying original_functio=decorator_function(original_function)
def original_function():
    print("This is original function")

original_function() ##Since we used @decorator_function above , so this is same as original_function=decorator_function(original_function). Its like we've decorated out original function with some additional functionalities via using decorators
#output:
#This is new functionlity added to wrapper_function without changing it
#This is original function




