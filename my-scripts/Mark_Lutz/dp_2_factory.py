#Creational Design pattern

'''
This is used when "A class cannot anticipate the type of objects its needs to create beforehand" i.e. a class requires its subclasses to specify the object it creates.
Goal  is to increase modularity of program i.e. having andividual classes doing their own goals
Allows us to decide on runtime, instance of which class we need to create
'''

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def person_method():
        pass
    
class Student(Person):
    def __init__(self):
        self.name = 'Basic Student Name'
    
    def person_method(self):
        print('Am a Student')

class Teacher(Person):
    def __init__(self):
        self.name = 'Basic Teacher Name'
    
    def person_method(self):
        print('Am a Teacher')
        
class Personfactory():
    #@abstractmethod
    def build_person(person_type):
        if person_type.lower() == 'student':
            return Student()
        elif person_type.lower() == 'teacher':
            return Teacher()
        else:
            raise "Error: Incorrect class name passed\n"

obj = Personfactory.build_person('student')
print(obj)
obj.person_method()
            
        
        
    

    
