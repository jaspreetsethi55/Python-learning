#!/usr/bin/python3.4

class Organization:
    
    organization_name = 'Genpact' ##class variable
    number_of_emp = 0
    raise_pay = 1.5

    def __init__(self,fname,lname,age,sex,pay): ##Intializer (constructor)
        self.first_name = fname.capitalize() #making First char of name in upper case
        self.last_name = lname.capitalize()
        self.age = age ##Instance variable 
        self.sex = sex.upper()
        self.pay = int(pay)
        self.email = fname + '.' + lname + '@' + Organization.organization_name + '.com'

        Organization.number_of_emp += 1 ##calling class variable by class name and not by self, as we know number of employees should not be specific for any employee

    def raise_sal(self):
        self.pay *= self.raise_pay ##calling class variable by self so that it can be specific to certain employee

    @classmethod ##Decorator are used to declare class methods
    def set_raise_sal(cls,pay):  ##In class methods, first argument is always class by default
        cls.raise_pay = pay

    @classmethod
    def from_string(cls,emp_str):
        fname,lname,age,sex,pay = emp_str.split(":")
        return cls(fname,lname,age,sex,pay) ##This will call Organization(fname,lname,sex,pay)

    @staticmethod ###Decorator are used to declare class methods
    def is_weekday(day): ##Static methods neither hv instance nor class as their first argument,so if we don't need instance/class inside methods then use static method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Organization('jaspreet','sethi',30,'M',5500000)
print(emp1.__dict__) #{'first_name': 'Jaspreet', 'last_name': 'Sethi', 'pay': 5500000, 'age': 30, 'sex': 'M', 'email': 'jaspreet.sethi@Genpact.com'}

emp2 = Organization('seth','meyer',45,'M',6500000)
print(Organization.number_of_emp) #2
print(emp1.number_of_emp)  #2
print(emp1.email) #jaspreet.sethi@Genpact.com

emp1.raise_sal() ##calling function via instance
print(emp1.__dict__) #{'first_name': 'Jaspreet', 'last_name': 'Sethi', 'pay': 8250000.0, 'age': 30, 'sex': 'M', 'email': 'jaspreet.sethi@Genpact.com'}

emp2.raise_pay = 1.25
emp2.raise_sal()
print(emp2.pay) #8125000.0

####Changing all emp raise_pay - calling class method via instance
Organization.set_raise_sal(1.5)   ##Similar effcet of Organization.raise_pay = 1.5
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.raise_pay) #1.5
print(emp2.raise_pay) #1.25 because we have emp2.raise_pay = 1.25 above and thus raise_pay is also now instance attribute for emp2 and will be there in emp2.__dict__

##We can even call classmethods by instance and it will have same effect as calling via class because inside classmethod we use class
emp2.set_raise_sal(1.75)
print(emp1.raise_pay)
print(emp2.raise_pay) ## Even now emp2.raise_pay = 1.25 as this is instance attribute

emp_str = 'Abhishek:Arnold:34:M:5600000'
emp3 = Organization.from_string(emp_str)
print(emp3.__dict__)

##using static method
import datetime

my_date = datetime.date(2019,4,9)
print(Organization.is_weekday(my_date))
