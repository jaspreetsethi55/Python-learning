#!/usr/bin/pyhton3.4

class Employee:

  raise_pay = 1.04 ##class variable
  emp_num = 0 ##class variable

  def __init__(self,fname,lname,pay):
    self.fname = fname
    self.lname = lname
    self.pay = pay
    self.email = fname  + '.' + lname + '@company.com'

    Employee.emp_num += 1

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  def raise_sal(self):
    self.pay = int(self.pay * self.raise_pay)

  ##print calls the str by default and if no str then repr
  ##repr shows an unambiguous form of object(that can easily re-create the object) and is used mostly by developers for debugging/logging/etc. It internaly calls __repr__
  ##str is meant to be more readable representaion of an object and is meant to be as an display to end user. It internaly calls __str__
  ##For more info on repr vs str, visit script str_vs_repr.py_
  def __repr__(self):
    return "Employee({},{},{})".format(self.fname,self.lname,self.pay)

  def __str__(self):
    return "{} - {}".format(self.fname + ' ' + self.lname,self.email)

emp1 = Employee('jaspreet','sethi',2500000)
emp2 = Employee('sumit','singhal',2500000)

##print(abc) by defaults calls print(str(abc)) to get string representaion of abc and if str(which calls __str__) fails then repr(which calls __repr__) acts as fallback

##So, below if we'll call print(emp1), this will actually call print(str(emp1)) i.e. print(__str__(emp1)) but since __str__ is not there so repr will act as fallback and since __repr__ is there, so it will call print(__repr__(emp1))

print(emp1) ##emp1.__str__() is called

##We can even call these special methods directly
print(repr(emp1)) ##emp1.__repr__() is called
print(str(emp1)) ##emp1.__str__() is called


print(1 + 2) #3
##Similary, + calls the special method __add__ 

print(int.__add__(1+2)) ##3 
print(str.__add__('a'+'b')) ##ab

#Thus integer use there own dunder add method which actually performs addition while string uses there own dunder add method which actually performs concatenation. Thus we can customize and make our own __add__ method in our class and change the behaviour of + (addition) as per our need

