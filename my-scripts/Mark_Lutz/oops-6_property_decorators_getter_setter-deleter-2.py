#!/usr/bin/pyhton3.4

class Employee:


  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  ##Property decorator allows us to define a method that we can access like an attribute. Below is "Getter' example

  @property ##Getter: This actually allows us to access method just like attribute i.e. we can access this vis self.email instead of self.email()
  def email(self):
    return "{}.{}@company.com".format(self.fname,self.lname)

  def fullname(self):
    return "{} {}".format(self.fname,self.lname)


emp1 = Employee('jaspreet','sethi')

print(emp1.fname) #jaspreet
print(emp1.lname) #sethi
print(emp1.email) #jaspreet.sethi@company.com
print(emp1.fullname()) #jaspreet sethi

##Now let us say, we want to change the first name of emp1 to 'jasveen'
emp1.fname = 'jasveen'

print(emp1.fname) #jasveen
print(emp1.lname) #sethi
print(emp1.email) #jasveen.sethi@company.com    ##Focus here - this will actually call our getter 'email' method 
print(emp1.fullname()) #jasveen sethi ##works fine

##Thus people using our class don't need to change code at their end and the changes will still be reflected at their end using @property decorator

##If we'll use @property above fullname method we can even call it as attribute i.e. self.fullname instead of self.fullname()
