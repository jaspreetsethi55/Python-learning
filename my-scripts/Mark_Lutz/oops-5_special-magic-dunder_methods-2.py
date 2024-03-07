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

  ##repr shows an unambiguous form of object(that can easily re-create the object) and is used mostly by developers for debugging/logging/etc. It internaly calls __repr__
  ##str is meant to be more readable representaion of an object and is meant to be as an display to end user. It internaly calls __str__
  ##For more info on repr vs str, visit script str_vs_repr.py_
  def __repr__(self):
    return "Employee({},{},{})".format(self.fname,self.lname,self.pay)

emp1 = Employee('jaspreet','sethi',2500000)
emp2 = Employee('sumit','singhal',2500000)

##print(abc) by defaults calls print(str(abc)) to get string representaion of abc and if str(which calls __str__) fails then repr(which calls __repr__) acts as fallback

##So, below if we'll call print(emp1), this will actually call print(str(emp1)) i.e. print(__str__(emp1)) but since __str__ is not there so repr will act as fallback and since __repr__ is there, so it will call print(__repr__(emp1))

print(emp1) ##emp1.__repr__() is called since __str__() is not there
#emp1 = Employee('jaspreet','sethi',2500000)


