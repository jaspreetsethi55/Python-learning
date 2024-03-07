#!/usr/bin/pyhton3.4

##Class Variables are variables that are shared among all instances of class while instance variables can be uniques for each instance like(E.g. emp1.fname created by instance variable self.fname is only for emp1) whereas class variables are same for all instances

class Employee:

  raise_pay = 1.04 ##class variable
  emp_num = 0 ##class variable

  def __init__(self,fname,lname,age,pay):
    self.name = fname
    self.lname = lname
    self.age = age
    self.pay = pay
    self.email = fname  + '.' + lname + '@company.com'

    Employee.emp_num += 1

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  def raise_sal(self):
    self.pay = int(self.pay * self.raise_pay)

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,250000)

print(emp1.emp_num)
print(emp2.emp_num)

print(emp1.pay)
print(emp2.pay)

emp1.raise_pay = 1.05

emp1.raise_sal()
emp2.raise_sal()

print(emp1.pay)
print(emp2.pay)
