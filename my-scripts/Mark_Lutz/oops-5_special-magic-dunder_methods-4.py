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
   
  ##+ calls the special method __add__. Thus our below dunder method gives sum of pay of 2 employee objects given to it
  def __add__(self,other):
    return self.pay + other.pay

  ####len calls special dunder method __len__ in background
  def __len__(self):
    return len(self.fname + self.lname)

emp1 = Employee('jaspreet','sethi',2500000)
emp2 = Employee('sumit','singhal',2500000)

print(emp1 + emp2) ## 5000000
##if we'll remove the above __add__ method from Employee class then above statement will give us error as it will doesn't know how to add 2 objects together

##len calls special dunder method __len__ in background i.e. len('test') actualy calls 'test'.__len__() in background
print(len(emp1)) ##will return len of fullname of emp1

##We can visit https://docs.python.org/3/reference/datamodel.html to see more special methods i.e. how python internally calls them and can overwrite these as per our need

