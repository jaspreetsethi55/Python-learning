class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print('Payroll for: {} - {}'.format(employee.id,employee.name))
            print('- Check amount: {}'.format(employee.calculate_payroll()))
            print('')

'''
Employee is the base class for all employee types. It is constructed with an id
and a name. What you are saying is that every Employee must have an id assigned
as well as a name
'''
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

'''
You create a derived class SalaryEmployee that inherits Employee. The class is initialized with the id and name required by the base class, and you use super() to initialize the members of the base class
'''
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

'''
The company also employs manufacturing workers that are paid by the hour, so you add an HourlyEmployee to the HR system
'''
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

'''
Finally, the company employs sales associates that are paid through a fixed salary plus a commission based on their sales, so you create a CommissionEmployee class
'''
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

#Since CommissionEmployee derives from SalaryEmployee, you have access to the weekly_salary property directly, and you could’ve implemented .calculate_payroll() using the value of that property.
#The problem with accessing the property directly is that if the implementation of SalaryEmployee.calculate_payroll() changes, then you’ll have to also change the implementation of CommissionEmployee.calculate_payroll(). It’s better to rely on the already implemented method in the base class and extend the functionality as needed.


