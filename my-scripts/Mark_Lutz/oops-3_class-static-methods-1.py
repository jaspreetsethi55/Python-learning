#!/usr/bin/pyhton3.4

##Regular methods in a class automatically take instance as a first argument and are thus known as instance methods
##Class methods take first argument as class 

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

  @classmethod ##We use Decorator for declaring class methods
  def set_raise_sal(cls,pay):
    ##We use 'cls'for class methods in the same way as we use 'self' for instance methods. 
    ##Although we can use any other keywords but these are just standards
    cls.raise_pay = pay

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,250000)

print(Employee.raise_pay) #1.04
print(emp1.raise_pay) #1.04
print(emp2.raise_pay) #1.04

Employee.set_raise_sal(1.25) ##For this example, this will do the same change as setting class variable raise_pay 'Employee.raise_pay = 1.25'

##Even below statement can be used and this will also change raise_pay for complete Employee class
##emp1.set_raise_sal(1.25) 

print(Employee.raise_pay) #1.25
print(emp1.raise_pay) #1.25
print(emp2.raise_pay) #1.25


Employee.raise_pay = 1.04
print(Employee.raise_pay) #1.04
print(emp1.raise_pay) #1.04
print(emp2.raise_pay) #1.04

emp1.set_raise_sal(1.07)
print(Employee.raise_pay) #1.07
print(emp1.raise_pay) #1.07
prin(emp2.raise_pay) #1.07
