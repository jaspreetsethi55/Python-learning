#!/usr/bin/pyhton3.4

##Class Variables are variables that are shared among all instances of class while instance variables can be uniques for each instance like(E.g. emp1.fname created by instance variable self.fname is only for emp1) whereas class variables are same for all instances

class Employee:

  raise_pay = 1.04 ##class variable
  def __init__(self,fname,lname,age,pay):
    self.name = fname
    self.lname = lname
    self.age = age
    self.pay = pay
    self.email = fname  + '.' + lname + '@company.com'

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  def raise_sal(self):
    ##self.pay = int(self.pay * raise_pay)
    ##This will give error when we will call emp1.raise_sal() i.e. 'raise_pay' is not defined because when we access any class variable, we either need to access it by class or by instance of class

    ##So we can either use Employee.raise_pay or self.raise_pay but both have different meanings
    ##Employee.raise_pay -- This will belong to whole class and we cannot change for any instance like emp1.raise_pay = 1.05
    ##we use Employee.raise_sal where we do not need to override value for any instance

    ##self.raise_pay -- We can change this for any instance i.e. epm1 or emp2. 
    ##This can be oveerridden by instance or by any other subclass. So we use self.raise_pay where we need to override value for any instance

    self.pay = int(self.pay * self.raise_pay)

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,200000)

print(emp1.pay)
print(Employee.__dict__)
print(emp1.__dict__)
print(emp1.raise_pay) ##emp1 does not have its own 'raise_pay' atribute, its accessing class 'raise_pay' atribute as its class variable and available to all instances
print(emp1.__dict__)

## This will change emp1.raise_pay and will also change emp1.pay as self.raise_pay will apply on emp1 i.e. we are accessing class variable but by our instance
emp1.raise_pay = 5
print(emp1.__dict__)
print(emp1.raise_pay)

print(emp1.__dict__)
emp1.raise_sal()

print(Employee.__dict__)
print(emp1.pay)
