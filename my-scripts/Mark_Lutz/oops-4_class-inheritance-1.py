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
  def from_string(cls,emp_str): ##usually these alternative constructor methods start from 'from' but that's just convention and we can use anything
    first,last,age,pay = emp_str.split(':') ##Internally changes to first,last,age,pay = emp_1_str.split(':')
    return cls(first,last,age,pay) ##Internally changes to Employee(first,last,age,pay)

  ##We want simple function that takes date and return whether its a weekday or not
  ##So this function actually has a logical connection with our 'Employee' class but its doesn't actually depend on any instance or class variable,so we need to make this as static method
  @staticmethod
  def is_weekday(day):
    if(day.weekday == 5 or day.weekday == 6):
      return False
    return True

  ##Sometimes people write regular methods or class methods that actually should be static methods
  ##just remember that you should use static method when you don't want to use instance or class anywhere in that method/function
  ##For e.g. in class  method 'from_string' if we haven't used 'cls' and just need to perform some other task in it then we should have used 'static method' and not 'class method'
  ##If we are not using self or cls in our regular methods then we should use static method


############Inheritance - Adding sub-classes########################
#Inheritance allows us to in-herit attributes and methods from parent class
#This is useful as we can create sub-classes and get all functionallity of our parent class and then we can overwrite or add complete new functionality without effecting the parent class

class Employee_test(Employee): ##By this class, 'Employee_test' will inherit all attributes/methods of class 'Employee'
  pass

##How it works: when we will initiate a instance of class 'Employee_test' by using "test1 = Employee_test('test','employee',30,250000)", then it will first search for an __init__ method in class 'Employee_test' and if not found then python will walk thru the 'chain of inheritance' until it founds the method(here __init__) we are looking for. This chain on finding requested method is called 'method resolutioner'

##help -- We can use help function to know/get the 'method resolution order' i.e. it tells how python looks for a certain method
##mro -- we can also use __mro__ to see the exact method resolution order. classname.__mro__

print(help(Employee_test)) ##This will give all info related to class 'Employee_test' i.e. how methods are resolved in it(hierarchy) and all other info like methods,name of variables,etc
exit()

class Developer(Employee):
  raise_pay = 1.15    

  ##Sometimes we need to initiate our subclass with more info then our parent class, for e.g. we need to add 'programming language' to developer instance
  def __init__(self,fname,lname,age,pay,prog_lang):
    super().__init__(fname,lname,age,pay) ##This is call __init__ method from base class(here Employee) of class 'Developer'. No need to pass self here
    #use Developer.__mro__ to know the exact mro that super() uses here.
    #If we use multiple inheritance then super() goes from left to right. class A(B,C): Then super().__init__() will be searched in A and if not found then we go to B. we can use A.__mro__ to know exact mro

    #Employee.__init__(self,fname,lname,age,pay) ##we can also use this for calling parent class __init__ method
    ##But try to use super as it is more maintainable and necessary in case of multiple inheritance

    self.prog_lang = prog_lang


class Manager(Employee):

  def __init__(self,fname,lname,age,pay,employees=None):
    super().__init__(fname,lname,age,pay)
    if employees:
        self.employees = employees
    else:
        self.employees = []

  def add_emp(self,emp):
    if emp not in self.employees:
      self.employees.append(emp)

   
  def remove_emp(self,emp):
    if emp in self.employees:
      self.employees.remove(emp)


  def print_emp(self):
    for emp in self.employees:
      print("{Emp:\nName:{name}\nEmail:{email}".format(name=self.fname+self.lname,email=self.email))


emp1 = Employee('jaspreet','sethi',30,250000)
emp2 = Employee('sumit','singhal',27,250000)

import datetime
my_date = datetime.date(2016,7,10)
my_date_2 = datetime.date(2016,7,11)

print(Employee.is_weekday(my_date))
print(Employee.is_weekday(my_date_2))

##using inherited class
test1 = Employee_test('test','employee',30,250000) ##
print(test1.email)
print(test1.pay)
print(test1.raise_sal()) #this will use raise_pay variable from Empployee class as we there is no raise_pay variable in Employee_test class.

emp_dev1 = Developer('Jas','Sethi',30,250000,'python')
emp_dev2 = Developer('Abhishek','Arnold',34,280000,'python')
print(test1.pay)
print(test1.raise_sal()) #this will use raise_pay variable from Developer class while raise_sal() method from Employee class

emp_mgr1 = Manager('Seth','Meyer',45,300000,[emp_dev1])
print(emp_mgr1.__dict__)

emp_mgr1.add_emp(emp_dev2)
print(emp_mgr1.__dict__)

emp_mgr1.remove_emp(emp_dev1)
print(emp_mgr1.__dict__)



###isinstance, issubclass###############
'''
The built-in functions isinstance and issubclass ask two different questions.

isinstance(object, classinfo) asks whether an object is an instance of a class (or a tuple of classes).
issubclass(class, classinfo) asks whether one class is a subclass of another class (or other classes).

In either method, classinfo can be a ?class, type, or tuple of classes, types, and such tuples.?

Since classes are themselves objects, isinstance applies just fine. We can also ask whether a class is a subclass of another class. But, we shouldn't necessarily expect the same answer from both questions.
'''

class Foo(object):
	pass

class Bar(Foo):
	pass

issubclass(Bar, Foo)
#>True

isinstance(Bar, Foo)
#>False     ## Bar is a subclass of Foo, not an instance of it. Bar is an instance of type which is a subclass of object, therefore the class Bar is an instance of object.

isinstance(Bar, type)
#>True
issubclass(type, object)
#>True
isinstance(Bar, object)
#>True

