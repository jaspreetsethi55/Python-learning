#!/usr/bin/python3.4

'''A function is said to have a side effect, if, in addition to producing a return value, it modifies the caller's environment in other ways. 
For example, a function might modify a global or static variable, modify one of its arguments, raise an exception, write data to a display or file and so on. 

There are situations, in which these side effects are intended, i.e. they are part of the functions specification. But in other cases, they are not wanted, they are hidden side effects.
'''

'''
Example: no side effects
Let's assume, we are passing a list to a function. We expect that the function is not changing this list. First let's have a look at a function which has no
side effects. As a new list is assigned to the parameter list in func1(), a new memory location is created for list and list becomes a local variable
'''
def no_side_effects(cities):
  print(cities)
  cities = cities + ["Birmingham", "Bradford"]
  print(cities)


locations = ["London", "Leeds", "Glasgow", "Sheffield"]
no_side_effects(locations)

'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield']
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
'''

print(locations)
'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield']
'''



'''
Example: side efects
This changes drastically, if we increment the list by using augmented assignment operator +=. To show this.
To be precise if we are making any in place change to passed mutable variable inside function(changes made to the same reference/address where varaiable is tired in memory) then it will also change that variable outside function.
we change the previous function rename it to "side_effects" in the following example:
'''
def side_effects(cities):
  print(cities)
  cities += ["Birmingham", "Bradford"] ##cities[0] = 'Noida' -- this will also change location[0] to 'Noida'
  print(cities)

locations = ["London", "Leeds", "Glasgow", "Sheffield"]
side_effects(locations)

'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield']
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
'''

print(locations)
'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield','Birmingham', 'Bradford']
 '''

'''We can see that Birmingham and Bradford are included in the global list locations as well, because += acts as an in-place operation.'''


'''Passing Shallow copy:
The user of this 'side_effects' function can prevent this side effect by passing a copy to the function(E.g. list.copy, [:] or deep copy in case of nested structures). A shallow copy is sufficient, because there are no nested structures in the list:
'''

def side_effects(cities):
  print(cities)
  cities += ["Birmingham", "Bradford"]
  print(cities)

locations = ["London", "Leeds", "Glasgow", "Sheffield"]
side_effects(locations[:])

'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield']
['London', 'Leeds', 'Glasgow', 'Sheffield', 'Birmingham', 'Bradford']
'''

print(locations)
'''output:
['London', 'Leeds', 'Glasgow', 'Sheffield']
'''



#######Practice Exercise###########
def func(a,city=[]):
	city += ['Noida']

	print(a,city)

c = ['Hyderabad','Delhi']

func(1,c)
print(c)

func(2,c)
print(c)

func(3)
print(c)


'''
1 ['Hyderabad', 'Delhi', 'Noida']
['Hyderabad', 'Delhi', 'Noida']
2 ['Hyderabad', 'Delhi', 'Noida', 'Noida']
['Hyderabad', 'Delhi', 'Noida', 'Noida']
3 ['Noida']
['Hyderabad', 'Delhi', 'Noida', 'Noida']
'''
