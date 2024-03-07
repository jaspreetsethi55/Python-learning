#!/usr/bin/pyhton3.4

##Property decorators allows our class to give getter, setter and deleter functionality

class Employee:


  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname
    self.email = fname  + '.' + lname + '@company.com'


  def fullname(self):
    return "{} {}".format(self.fname,self.lname)

'''
  def email(self):
    return "{}.{}@company.com".format(self.fname,self.lname)
'''

emp1 = Employee('jaspreet','sethi')

print(emp1.fname) #jaspreet
print(emp1.lname) #sethi
print(emp1.email) #jaspreet.sethi@company.com
print(emp1.fullname()) #jaspreet sethi

##Now let us say, we want to change the first name of emp1 to 'jasveen'
emp1.fname = 'jasveen'

print(emp1.fname) #jasveen
print(emp1.lname) #sethi
print(emp1.email) #jaspreet.sethi@company.com    ##Focus here - email still hvaing old name
print(emp1.fullname()) #jasveen sethi ##works fine

##Thus email is still jaspreet.sethi@company.com while we want it as jasveen.sethi@company.com since we changed the fname of emp1 to 'jasveen' while our method fullname() works give and returns new full name since it grabs fname and lname everytime being called.

#So, people using our class don't want to change the email at their end everytime, thus we need to fix this in class. So, our first thought to fix this will be to create a new email() method(as commented above and remove self.email from __init__) to return email(similar to fullname()) but even then it will break the code for people using our class as they have to call emp1.email() while currently they would be using emp1.email, so we need to do something in our class itself and this is exactly where languages like Java uses getters and setters and in python, we can use the same getters/setters concept using property decorators


