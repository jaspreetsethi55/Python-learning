#!/usr/bin/pyhton3.4

class Employee:


  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  ##Property decorator allows us to define a method that we can access like an attribute. Below is "Getter' example

  @property ##Getter: This actually allows us to access method just like attribute i.e. we can access this vis self.email instead of self.email()
  def email(self):
    return "{}.{}@company.com".format(self.fname,self.lname)

  @property
  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

  @fullname.setter ##This is setter. As shown above @property should also be used above fullname method, only then setter will implement here 
  def fullname(self,name):
    self.fname,self.lname = name.split( )


emp1 = Employee('jaspreet','sethi')

##Now we need to do kind of opposite what we have done in setter i.e. we need change the method value first and need need to change the attributes as per it. For instance, below we changed fullname method(accessed like attribute i.e. getter) and now we need to chngae attributes fname and lname as per it. This is exactly where setters come in to effect and we can make a same name function('fullname') and use @fullname.setter above it, this will make and work it as a setter
emp1.fullname = 'jasveen sethi'

print(emp1.fname) #jasveen
print(emp1.lname) #sethi
print(emp1.email) #jasveen.sethi@company.com
print(emp1.fullname) #jasveen sethi

