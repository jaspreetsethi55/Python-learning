#!/usr/bin/python3.4

def get_exponential(x):
    def get_exponential_object(n): ##This function maintains state-information i.e. it remembers all local global variables it uses
        return x ** n             ##State retention is done by storing packets of memory i.e. function get_exponential_object will store 'x' in memory
    return get_exponential_object

func_square_object1 = get_exponential(2)
print(func_square_object1(2)) #4
print(func_square_object1(3)) #8

func_square_object2 = get_exponential(3) ##Each object maintains it's own state and is indenpendent of other object
print(func_square_object2(2)) #9
print(func_square_object2(3)) #27



##above closure can also be implemented using lambda(anonymous functions)
def get_expo(x):
    return lambda n : x ** n ##lambda are unmamed functions. 

func_square_object1 = get_expo(2)
print(func_square_object1(2)) #4
print(func_square_object1(3)) #8

func_square_object2 = get_expo(3)
print(func_square_object2(2)) #9
print(func_square_object2(3)) #27


##Above functions will not work in python 2.2 and earlier s there was no concept of enclosed scopes(non local) at that time, so we need to use 'defualts' in case we need to use in earlier python versions
def get_exponential(x):
    def get_exponential_object(n,x=x): ##we are passing defaults i.e. x-x, this will work in all python versions(earlier+current)
        return x ** n
    return get_exponential_object

func_cube_object = get_exponential(3)
print(func_cube_object(2)) #9
print(func_cube_object(3)) #27


##Factory Functions in loop - strange behaviour - only take last loop variable
def get_results(x):
    res = []
    for i in range(x):
        res.append(lambda n : i ** n)
    return res

results = get_results(5)
print(results) ##This is list of functions
##[<function get_results.<locals>.<lambda> at 0x7f29929c1d08>, <function get_results.<locals>.<lambda> at 0x7f29929c1d90>, <function get_results.<locals>.<lambda> at 0x7f29929c1e18>, <function get_results.<locals>.<lambda> at 0x7f29929c1ea0>, <function get_results.<locals>.<lambda> at 0x7f29929c1f28>]

print(results[0](2)) ## 16 #it should be 0 ** 2 = 0 but it is 4 ** 2 = 16 as it only remembers last accessed variable in for loop
print(results[1](2)) ## 16 but it should be 1
print(results[2](2)) ## 16 but it should be 4


##Factory Functions in loop - use defaults for remember each loop variable
def get_correct_results(x):
    res = []
    for i in range(x): 
        res.append(lambda n,i=i : i ** n) #We used default here x=x coz defaults are evaluated when nested function is created(and thus will remember all var's) and not                                          #when called
    return res

results = get_correct_results(5)

print(results[0](2)) ## 0 
print(results[1](2)) ## 1
print(results[2](2)) ## 4 



