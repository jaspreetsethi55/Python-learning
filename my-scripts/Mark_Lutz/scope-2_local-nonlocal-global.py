#!/user/bin/python3.4

def student(lname,lage): ##Local variable
    print("Local variable:{} {}".format(lname,lage)) ## Local variable:Jaspreet 28

    lname = 'Jaspreet Sethi'  ##This will only change local variable 'lname' and not global variable lname = 'Sethi'
    lage = 29

    print("Local variable:{} {}".format(lname,lage)) ##Local variable:Jaspreet Sethi 29

    ##If we want to access/change global variable name/age here, then we need to use 'global' keyword
    #global lage 
    '''Above statement will give us either error/warning as follows:
      SyntaxWarning: name 'lage' is assigned to before global declaration
      SyntaxError: name 'lage' is parameter and global

    This also explains why it is an error: to declare a variable as global, you are not allowed to have used that variable name previously in the same scope (presumably because it would be confusing for the global statement to make assignments before it go to the global variable, and Python doesn't support the same name being both global and local in the same scope).
    i.e. for a given block of code with its own scope, you can't have variables that are both in the local namespace and the global namespace
    '''

    ##Accessing Global variable
    print("Acessing Global variable:{} {}".format(name,age))

    '''Although above line will print the globle variable 'name' but will still give below warning(error in python 3.7 and above):
     SyntaxWarning: name 'name' is used prior to global declaration
       global name

    We can use 'global name' above this line, to tell the code thatt we'll be acessing the global 'name'


    ##We are actually using 'global name' below so as to modify 'name', if we will not modify global 'name' as below then there is no need to use 'global name' to access global variable and in that case it will also not give us any warning

    **So, if we are just accessing global/nonlocal var then there is no need to use global or nonlocal keyword
    **global or nonlocal keyword are used when we need to modify global or  encloseed variable else we'll get an error
    **if we are first accessing and then modifying global/nonlocal variable then we used use global or nonlocal keyword(as per requirement) before both these tasks i.e. if we'' use global or nonlocal keyword(after acessing and before modifying)  then we'll get warning 'global declaration' warning as ahown above
    '''

    ##Changing Global variables
    global name
    name = 'Jaspreet Sethi'
    print("Global name:{}".format(name))

    def modify_student(iname,iage = 25): ##iname,iage are local to this function
        
        ##Accessing Enclosed variables
        nonlocal lname ## nonlocal used before acessing enclosed var 'lname' to avoid warning/error, same reason as shown above 
        print("Enclosed variable:{} {}".format(lname,lage))

        ##Changing Enclosed variable
        ##This will work because we've used nonlocal above, else we'll get error
        lname = iname
        print("Enclosed variable:{} {}".format(lname,lage))

        ##Declaring a new global name from inside function
        global global_name
        global_name = 'student'

    return modify_student

name = 'Jaspreet' ##Global Variable
age = 28 ##Global variable
lname = 'Sethi'

student_1 = student(name,age)
student_1('Jaspreet Singh Sethi')
print("Global var declared from inside function:{}".format(global_name))
