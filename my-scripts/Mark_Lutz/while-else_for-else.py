#!/usr/bin/python3.4

#####while/else and for/else loops
#else statements are only not executed when break statement is executed(used and satisfied as per condintion) inside while loop
#In all other conditions else condition will be executed.
#Even when while loop condition is not fulfilled at all, even then else will be executed


#break will execute in below case and else will not
var = 5;
l = [4,10,15]
while var >= 1:
    if var in l:
        print("{} found in list{}".format(var,l))
        break ##If break is executed it means 'else' will be skipped
    var -= 1
else:
    print("{} not found in list{}".format(var,l))

    
#break will not execute in below case and thus else will execute
var = 5;
l = [6,10,15]
while var >= 1:
    if var in l:
        print("{} found in list{}".format(var,l))
        break
    var -= 1
else:
    print("{} not found in list{}".format(var,l))


#else will executed as while loop completes without 'break' being encountered
var = 5;
while var >= 1:
    var -= 1
else:
    print("Else executes")

#else will executed even when while condition is not satisfied even once
var = 5;
while var >= 6:
    var -= 1
else:
    print("Else executes")


