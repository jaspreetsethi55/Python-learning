#!/usr/bin/python3.4

##Ordering rules/steps: Arguments must follow below rule(in sequential order as mentioned) or else python will give us an error.
    #In function call:
        #Any positional argument
        #Any keyword argument(name=value)
        #*iterable form -- unpacking
        #**dict form -- unpacking

    #In function header:
        #Normal arguments(name)
        #Default Argument(name=value)
        #*iterable form -- collecting or *(in 3.X)
        #keyword only arguments(specific to 3.X)
        #**form - collecting from **

##Resolving rules/steps
    #Assigned non-keyword arguments by position
    #Assigned keyword arguments by name
    #Assigned extra non-keyword arguments to *named tuple
    #Assigned extra keyword arguments to **named dict
    #Assigned default values to un-assigned arguments in header

##1. Positional: matched from left to right

def positional(a,b):
    print(a,b)

x,y = 1,2
positional(x,y) ##1 2


##2: Keywords: matched by argument name

def keywords(a,b):
    print(a,b)

x,y = 1,2
keywords(b=y,a=x) ##Order doesn't matter if we are calling function via keyword arguments


##3. Defaults: specify values for options arguments that aren't passed

def defaults(a,b,c=3,d=4):
    print(a,b,c,d)

x,y = 1,2
defaults(b=y,a=x) #1 2 3 4
defaults(x,b=y,c=x) #1 2 1 4
#defaults(c=y,d=x,a,b) #This will give "SyntaxError: non-keyword arg after keyword arg" as this doesn't follows the ordering rules of function calling


##4. varargs collecting(in function header): collecting arbitrarily many positional arguments or keyword arguments
    #*args: collects in tuple
    #**args: collects in dictionary

def collecting_tuple_args(*args): ##collecting in tuple
    print(args)
collecting_tuple_args(1,2,3,4) #(1, 2, 3, 4)

def collecting_dict_args(**args): ##collecting in dictionary
    print(args)
collecting_dict_args(a=1,b=2,c=3,d=4) #{'c': 3, 'd': 4, 'a': 1, 'b': 2}

def collecting_args(*pargs,**kargs):
    print(pargs,kargs)
collecting_args(1,2,c=3,d=4) #(1, 2) {'d': 4, 'c': 3}

def collecting_misc_args(a,b=2,*pargs,**kargs):
    print(a,b,pargs,kargs)
collecting_misc_args(1,2,3,d=4,e=5) #1 2 (3,) {'d': 4, 'e': 5}


##5. varargs unpacking(in function call): passing arbitrarily many positional arguments or keyword arguments
    #*args - unpacks collection. E.g. tuple,list,etc
    #**args - unpacks dictionary

def unpacking_args(a,b,c,d):
    print(a,b,c,d)

tup = (1,2,3,4)
dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

unpacking_args(*[1,2,3,4]) #1 2 3 4
unpacking_args(*tup) #1 2 3 4
unpacking_args(**dictionary)  #1 2 3 4
unpacking_args(*dictionary)  #a b c d ##as by default dictionary returns all his keys when used as a iterable directly
unpacking_args(*(1,2),**{'c':3, 'd':4}) #1 2 3 4
unpacking_args(1,*(2,),c=3,**{'d':4}) #1 2 3 4


##In python2.x there was also a function named as 'apply' - used to call function via args and kargs arguments
pargs = (1,2)
kargs = {'c':4, 'd':5}
unpacking_args(*pargs,**kargs)
#apply(unpacking_args,pargs,kargs) #This is same as unpacking_args(*pargs,**kargs) but doesn't works in python3.x


##6. keyword-only arguments(only in 3.x): We can force any arguments in the function header to be keyword arguments, below are contions for it:
    #In function header:
        #It should be after *args argument(and before **args if **args is also there)
        #we also give * as an argument and all arguments passed after * will be keyword-only arguments
    #In function call:
        #keyword only argument must appear before or after *args but always before **args. Can also be included in **args

def keyword_only(a,b=2,*args,f):
    print(a,b,args,f)

#keyword_only(1,(3,4),6) #Error: TypeError: keyword_only() missing 1 required keyword-only argument: 'f' 
keyword_only(1,(3,4),f=6) #1 (3, 4) () 6
keyword_only(1,*(3,4),f=6) #1 3 (4,) 6
keyword_only(1,*(3,4),**{'f':6}) #1 3 (4,) 6

def keyword_only_2(a,b,*,d,e=4): #here d, e are keyword only arguments
    print(a,b,d,e)

keyword_only_2(1,2,d=3,e=5) #1 2 3 5
keyword_only_2(1,2,d=3)   #1 2 3 4
keyword_only_2(*(1,2),**{'d':4,'e':5})  #1 2 4 5
