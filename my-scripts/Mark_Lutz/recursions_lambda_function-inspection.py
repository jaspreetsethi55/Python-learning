#!/usr/bin/python3.4


################recursion#######################
'''Make a recursive fucntion to get sum of below nested data structure'''
list_num = [ 1, 2, [1,2,3], [1,2], 5, 6, [7,8], [[9,10],11] ]

def recursive_sum(list_num):
    list_sum = 0
    for num in list_num:
        if isinstance(num,list):
            list_sum += recursive_sum(num) ##recursion
        else:
            list_sum += num
    return list_sum

print(recursive_sum(list_num))


##Doing above task without recursion##

def stack_sum(list_num):
    list_sum = 0
    for num in list_num:
        if isinstance(num,list):
            list_num.extend(num) ##main logic
        else:
            list_sum += num
    return list_sum

print(stack_sum(list_num))


###########Function inspection##################
#name of functions
print(recursive_sum.__name__) #recursive_sum
print(stack_sum.__name__) #stack_sum

#we can also apply 'dir' on our made functions, in same way as we applt to in-built functions
print(dir(recursive_sum))
'''
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''

#function script name and it's code starting line
print(recursive_sum.__code__) #<code object recursive_sum at 0x7f484a3ce0c0, file "recursions_lambda_function-inspection.py", line 8>

#function code attributes
print(dir(recursive_sum.__code__))
'''
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
('list_num', 'list_sum', 'num')
'''

print(recursive_sum.__code__.co_varnames) #('list_num', 'list_sum', 'num')
print(recursive_sum.__code__.co_argcount) #1

#function attributes
recursive_sum.final_sum = 68
recursive_sum.message = 'This is recursive function'
print(dir(recursive_sum)) #Note 'final_sum' and 'message' in last of below output
'''
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'final_sum', 'message']
'''

#function annotations(only in python3x, not on 2x)
#without annotations
def my_sum(w,x,y,z):
    return w+x+y+z
print(my_sum(1,2,3,4)) #10
print(my_sum.__annotations__) #{}

#with annotations
'''annotations are just kind of 'syntax header' for function arguments, they does nothing to function'''
def my_new_sum(w, x:'spam', y:(1,10), z:float) -> int:
    return w+x+y+z
print(my_new_sum(1,2,3,4)) #10
print(my_new_sum.__annotations__) #{'x': 'spam', 'return': <class 'int'>, 'y': (1, 10), 'z': <class 'float'>}

'''We can use argument defaults as we use normally with annotaions'''
def my_new_sum(w=1, x:'spam'=2, y:(1,10)=3, z:float=4) -> int:
    return w+x+y+z
print(my_new_sum()) #10
print(my_new_sum.__annotations__) #{'x': 'spam', 'return': <class 'int'>, 'y': (1, 10), 'z': <class 'float'>}


