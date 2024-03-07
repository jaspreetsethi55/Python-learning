#!/usr/bin/pyhton3.4

class Employee:

  raise_pay = 1.04 ##class variable
  emp_num = 0 ##class variable

  def __init__(self,fname,lname,pay):
    self.name = fname
    self.lname = lname
    self.pay = pay
    self.email = fname  + '.' + lname + '@company.com'

    Employee.emp_num += 1

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  def raise_sal(self):
    self.pay = int(self.pay * self.raise_pay)

emp1 = Employee('jaspreet','sethi',30)
emp2 = Employee('sumit','singhal',27)

##Special methods: 
#Also known as magic methods.
#These allow us to emulate some built-in's within python
#This is also how we implement operator overloading. In python 1+2 = 3, while 'a' + 'b' = 'ab' i.e. when we add 2 integers, we get their sum while when we add 2 strings, we get their concatenation. Thus same operator works differently for different objects. This is known as operator overloading.

print('a' + 'b') #ab
print(1+2) #3


#Also, if we'll print our emp instance
print(emp1) #<__main__.Employee object at 0x7fdf95fe9128>

##Thus print(emp1) print some vague employee object, it would be great if we can change this behaviour to print some meaningful info out of it. And this is where magic/dunder methods come in to effect i.e. by defining out own special method, we can change the built in behavaiour and operations

##These special methods are sorrounded by __(double underscore) and lot of people call __ as dunder, thus we oten call them dunder methods. E.g. dunder init means 'init methods sorrunded by __ i.e. __init__' as init is also special/dunder method as it is automatically called when we call our class and sets the attributes for us.




