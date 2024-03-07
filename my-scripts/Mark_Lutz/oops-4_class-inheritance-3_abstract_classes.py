'''
Concrete Classes:
These are normal classes which can be instantiated as well as inherited.

Abstract Classes:
Abstract base classes exist to be inherited, but never instantiated. Python provides the abc module to define abstract base classes.

Note: You can use leading underscores in your class name(private class) to communicate that objects of that class should not be created. Underscores provide a friendly way to prevent misuse of your code, but they don’t prevent eager users from creating instances of that class.

The abc module in the Python standard library provides functionality to prevent creating objects from abstract base classes.
'''

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    ##Abstract method: same concept as abstract classes i.e. classes inherting this class must override the .calculate_payroll() abstract method
    @abstractmethod
    def calculate_payroll(self):
        pass

class test(Employee):
    def __init__(id, name):
        super().__init__(self, id, name)
'''
You derive Employee from ABC, making it an abstract base class. Then, you decorate the .calculate_payroll() method with the @abstractmethod decorator.

This change has two nice side-effects:
1. You’re telling users of the module that objects of type Employee can’t be created.
2. You’re telling other developers working on the any other module that if they derive from Employee, then they must override the .calculate_payroll() abstract method.
'''

#employee = Employee(1, 'abstract') ##This will give error since employee is an abstract class so cannot be initiated directly
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Employee with abstract methods 
calculate_payroll
'''

##but we can use Employee class object via inheritance
employee = test(1, 'Sethi')
print(employee)


