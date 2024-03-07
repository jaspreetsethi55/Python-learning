#!/usr/bin/pyhton3.4

class Employee:

##__init__ is an initialize method used to initialze an instance of a class and by default always takes 'self' i.e. object/instance as a first argument
##This is similar to constructor in other programming languages
  def __init__(self,fname,lname,age):
    self.fname = fname  ##instance variables. These are set using self argument. 'self' is just a name, we can use any other name but 'self' is standarized
    self.lname = lname  ##We can use self.last = lname but its good to keep instance variable and argument name similar for readability purpose
    self.age = age
    self.email = fname  + '.' + lname + '@company.com'

##Each method withing class automatically takes self(i.e. object/instance) as the first argument
  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

emp1 = Employee('jaspreet','sethi',30)
emp2 = Employee('sumit','singhal',27)

print(emp1)
print(emp2)

print(emp1.fname) ##Accessing Attributes
print(emp2.fname)

print("{} {}".format(emp1.fname,emp1.lname))

##Notice parenthesis here because this is a method and not an attribute
full_name = emp1.fullname()  ##Accessing Method
print(full_name)

##These are exactly same
emp1.fullname() ## No need to pass self as we are calling by instance emp1 
Employee.fullname(emp1) ## We need to pass the instance as class 'Employee' doesn't know for which instance(self) we are calling method 'fullname'

##When code runs internaly 'emp1.fullname()' is converted to 'Employee.fullname(emp1)' and then executed
