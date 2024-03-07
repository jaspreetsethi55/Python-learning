#!/usr/bin/pyhton3.4

##We do often use class methods as alternative constructors i.e. we can use class methods in order to provide multiple ways to create our object
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
    cls.raise_pay = pay

  @classmethod
  def from_string(cls,emp_str): ##usually these alternative constructor  methods startfrom 'from' but that's just convention and we can use anything
    first,last,age,pay = emp_str.split(':') ##Internally changes to first,last,age,pay = emp_1_str.split(':')
    return cls(first,last,age,pay) ##Internally changes to Employee(first,last,age,pay)

emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',27,250000)

##let us say we are now getting the employee info as a string
emp_1_str = 'jaspreet:sethi:30:250000'
emp_2_str = 'sumit:singhal:27:250000'

first,last,age,pay = emp_1_str.split(':')
new_emp_1 = Employee(first,last,age,pay)

print(new_emp_1.name + ' ' + new_emp_1.lname)
print(new_emp_1.email)

##But it's not feasible to follow the above process of spliting emp string info(E.g. emp_1_str) for each employee and then creating its object
##So we can create an alternative constructor(class method) named as 'from_string' that can allow us to pass emp info as string and can create an object for that emp for us

new_emp_1 = Employee.from_string(emp_1_str)
new_emp_2 = Employee.from_string(emp_2_str)

print(new_emp_1.name + ' ' + new_emp_1.lname)
print(new_emp_1.email)
print(new_emp_2.name + ' ' + new_emp_2.lname)
print(new_emp_2.email)

