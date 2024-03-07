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
    ##self.raise_pay -- We can change this for any instance i.e. emp1 or emp2

    self.pay = int(self.pay * Employee.raise_pay)

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',2,200000)

print(emp1.pay)

print(emp1.__dict__)
print(emp1.raise_pay) ##emp1 does not have its own 'raise_pay' atribute, its accessing class 'raise_pay' atribute as its class variable and available to all instances
emp1.raise_pay = 5 ## This will change emp1.raise_pay but will not change emp1.pay as Employee.raise_pay will apply on emp1
print(emp1.raise_pay)
print(emp1.__dict__)

print(Employee.__dict__)

emp1.raise_sal()
print(emp1.pay)


'''
Output:

250000
{'name': 'jaspreet', 'lname': 'sethi', 'age': 30, 'pay': 250000, 'email': 'jaspreet.sethi@company.com'}
1.04
5
{'name': 'jaspreet', 'lname': 'sethi', 'age': 30, 'pay': 250000, 'email': 'jaspreet.sethi@company.com', 'raise_pay': 5}
{'__module__': '__main__', 'raise_pay': 1.04, '__init__': <function Employee.__init__ at 0x7faf200f4670>, 'fullname': <function Employee.fullname at 0x7faf200f4700>, 'raise_sal': <function Employee.raise_sal at 0x7faf200f4790>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
260000
'''
