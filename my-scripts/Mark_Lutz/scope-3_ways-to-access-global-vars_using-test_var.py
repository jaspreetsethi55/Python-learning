#!/usr/bin/python3.4

##Way 1(withing same module) - By default getting global value
def local():
    print(x) #80


##Way 2(within same module) - using Global
def use_global():
    global x
    x+=1
    print(x) #81


##Way 3(within different module) - using import
def from_module():
    import test_var
    print(test_var.x) #99

    test_var.x += 1
    print(test_var.x) #100

##Way 4(within different module) - using sys
def from_module_using_sys():
    import sys
    var = sys.modules['test_var']
    var.x+=1
    print(var.x) #101


x = 80

print(x) #80

local()
use_global()
from_module()
from_module_using_sys()
