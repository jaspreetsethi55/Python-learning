#!/usr/bin/python3.4

'''Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object Reference" or "Call by Sharing".

Passing immutable arguments(call by value): 
If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value. The object reference is passed to the
function parameters. They can't be changed within the function, because they can't be changed at all, i.e. they are immutable, so the effect is much like makking a copy

Passing mmutable arguments(call by pointer):
They are also passed by object reference, but they can be changed in place in the function. If we pass a list to a function, we have to consider two cases: 
  Elements of a list can be changed in place, i.e. the list will be changed even in the caller's scope.
  If a new list is assigned to the name, the old list will not be affected, i.e. the list in the caller's scope will remain untouched
'''

def student_name(name): 
  '''let's have a look at the string(immutable) variables. The parameter inside of the function remains a reference to the arguments variable, as long as the parameter   is not changed. As soon as a new value will be assigned to it, Python creates a separate local variable. The caller's variable will not be changed this way.
  Also, when talking about scope, each function run has its own set of local varibles i.e. variables inside any function are local to that function or any function enclosed in that function and they live only the time function is running. In case outside code need to use any of these local variabke, we need to use 'global'
  '''
  
  print("name=",name," id=",id(name))

  '''id(obj) returns the "identity" of the object "obj". This identity, the return value of the function, is an integer which is unique and constant for
  this object during its lifetime. Two different objects with non-overlapping lifetimes may have the same id() value'''

  name = 'sethi'
  print("name=",name," id=",id(name))

  return 'Student is {}'.format(name)

name = 'jaspreet'
print("name=",name," id=",id(name))
print(student_name(name))

'''output=
name= jaspreet  id= 140135099886000
name= jaspreet  id= 140135099886000
name= sethi  id= 140135099856744
Student is sethi


We can see that in the main scope, name has the identity 140135099886000. In the first print statement of the student_name() function, the name from the main scope is used, because we can see that we get the same identity. After we have assigned the value 'sethi' to name, name gets a new identity 140135099856744, i.e. a separate memory location from the global name. So, when we are back in the main scope name has still the original value 'jaspreet'

This means that Python initially behaves like call-by-reference, but as soon as we are changing the value of such a variable, i.e. as soon as we assign a new object to it, Python "switches" to call-by-value. This means that a local variable name will be created and the value of the global variable name will be copied into it. 
'''

