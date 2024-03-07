#!/usr/bin/python3.4

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
    self.pay = int(self.pay * raise_pay)
    ##This will give error when we will call emp1.raise_sal() i.e. 'raise_pay' is not defined because when we access any class variable, we either need to access it by class or by instance of class


emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,200000)

print(emp1.pay)
emp1.raise_sal()
print(emp1.pay)
