'''
Notice how the Employee base class doesn’t define a .calculate_payroll() method. This means that if you were to create a plain Employee object and pass it to the PayrollSystem, then you’d get an error. You can try it in the Python interactive interpreter:
'''

import hr
employee = hr.Employee(1, 'Invalid')
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([employee])

'''
Payroll for: 1 - Invalid
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/hr.py", line 39, in calculate_payroll
        print(f'- Check amount: {employee.calculate_payroll()}')
AttributeError: 'Employee' object has no attribute 'calculate_payroll'
'''

#While you can instantiate an Employee object, the object can’t be used by the PayrollSystem. Why? Because it can’t .calculate_payroll() for an Employee. To meet the requirements of PayrollSystem, you’ll want to convert the Employee class, which is currently a concrete class, to an abstract class. That way, no employee is ever just an Employee, but one that implements .calculate_payroll().
