#!/usr/bin/python3.4

class employee:
  pass

emp1 = employee()
emp2 = employee()

##instance variable contains data that is unique to each instance. E.g. emp1.fname is instance-variable of instance emp1 whereas fname is attribute

##Manually creating instance variables. Although we should create instances variable automatically always with '_init_' method
emp1.fname = 'jaspreet'
emp1.lname = 'sethi'
emp1.age = 30


emp2.fname = 'sumit'
emp2.lname = 'singhal'
emp2.age = 27

print(emp1)
print(emp2)

print(emp1.fname)
print(emp2.fname)
