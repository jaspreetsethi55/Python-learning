#!/usr/bin/pyhton3.4

##Class Variables are variables that are shared among all instances of class while instance variables can be uniques for each instance like(E.g. emp1.fname created by instance variable self.fname is only for emp1) whereas class variables are same for all instances

class Employee:

  def __init__(self,fname,lname,age,pay):
    self.name = fname
    self.lname = lname
    self.age = age
    self.pay = pay
    self.email = fname  + '.' + lname + '@company.com'

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  def raise_sal(self):
    self.pay = int(self.pay * 1.04) ##Ideally this(1.04) should be defined in some variable. We'll see this in next exercise

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,200000)

print(emp1.pay)
emp1.raise_sal()
print(emp1.pay)

##But ideally we should be using some below standards to get the raise salary
## emp1.raise_sal  ## This should be there for instance emp1
## Employee.raise_sal ## this should be there for all instances of class Employee
