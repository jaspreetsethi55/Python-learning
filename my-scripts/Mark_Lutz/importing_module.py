#!/usr/bin/python3.4

##when we import a file/module, its actually run all of the code of the file/module we are importing
import my_module

courses = ['science', 'maths', 'english']
print(my_module.var) ##we need to specify the module name with any var/function we are using from that module

index = my_module.find_index(courses,'maths') ##we need to specify the module name with any var/function we are using from that module
print(index)

#########################################################
## 'as' keyword, used for making alias
import my_module as mm 

print(mm.var) ## we can just use 'mm' now in place of complete module name

index = mm.find_index(courses,'maths')
print(index)


#########################################################
## 'from' keyword, importing only needed var/functions and not using module name while calling var/func
from my_module import find_index ##This will only import func find_index and not any other var/func

#print(var) #This will give error as we have only imported 'find_index' from my_module

index = find_index(courses,'maths') ## we don't need to specify the module name now as we have already speficy above in the import statement
print(index)

##############using 'from' keyword for importing multiple var/functions + 'as' keyword
from my_module import find_index as fi, var

index = fi(courses,'maths') #but note that this may not be much readable, so don't name anything that may confuse others regarding usage
print(index)

###############using 'from' keyword to import everything
from my_module import * ##but not a very good way, as it's difficult to say that what come from the module we have imported and what from our own script and thus make it hard to track down the problems

print(var)

index = find_index(courses,'maths')
print(index)



####when we import a module - how it finds where is the module
##when we import a module, it checks multiple locations and all these location are in list 'sys.path', we can see this list as below:

import sys
print(sys.path) #by default our current directory(directory from where we are running the script) is the first in which it looks unless we intentionally alter sys.path and change it
                ##Then it looks in python env variable 'PYTHONPATH' followed by python standard library paths.
                ##In the end it looks in to site-package directory i.e. the directory where we install 3rd party libraries



#######importing modules from different directory using sys.path
import sys
sys.path.append('/tmp/jsethi/python/Mark_Lutz/Modules') ## We can append/insert the directory path(where module to be used is kept) in sys.path

print(sys.path) ## Now sys.path will also contain '/tmp/jsethi/python/Mark_Lutz/Modules' 

import my_module_2

#Although above way suffice our need but is not the best way as we are updating sys.path before other import statements and also if this directory path is used in multile scripts and in case this changes then we need to make changes to all scripts
#Better way is to use python env variable PYTHONPATH, we can add below line to ~/.bash_profile file and then restart terminal or use command 'source ~/.bash_profile'
#export PYTHONPATH="/tmp/jsethi/python/Mark_Lutz/Modules" ##This path now will be added to sys.path automatically
#Once exported as shown above , we can just use 'import my_module_2'




