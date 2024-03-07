#!/usr/bin/pyhton3.4

##when working with classes Regular methods, they automatically pass takes first argument as instance of class i.e 'self' and are known as instance methods
##class methods automatically pass first argument 'cls' as class name and are thus known as class methods 
##Static methods don't pass anything automatically i.e. neither instance nor class. Infact we include them in class because they have some logical connection with class

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
  def from_string(cls,emp_str): ##usually these alternative constructor  methods startfrom 'from' but taht's mjust convention and we can use anything
    first,last,age,pay = emp_str.split(':') ##Internally changes to first,last,age,pay = emp_1_str.split(':')
    return cls(first,last,age,pay) ##Internally changes to Employee(first,last,age,pay)

  ##We want simple function that takes date and return whether its a weekday or not
  ##So this function actually has a logical connection with our 'Employee' class but its doesn't actually depend on any instance or class variable, so we need to make   this as static method
  @staticmethod
  def is_weekday(day):
    if(day.weekday == 5 or day.weekday == 6):
      return False
    return True

  ##Sometimes people write regular methods or class methods that actually should be static methods
  ##just remember that you should use static method when you don't want to use instance or class anywhere in that method/function
  ##For e.g. in class  method 'from_string' if we haven't used 'cls' and just need to perform some other task in it then we should have used 'static method' and not 'class method'
  ##If we are not using self or cls in our regular methods then we should use static method


emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',27,250000)

import datetime
my_date = datetime.date(2016,7,10)
my_date_2 = datetime.date(2016,7,11)

print(Employee.is_weekday(my_date))
print(Employee.is_weekday(my_date_2))
