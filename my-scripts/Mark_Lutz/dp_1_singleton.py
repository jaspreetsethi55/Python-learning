##Creational Design pattern

'''
When we need only onde instance of class, then we can use this design pattern.
Example: Connection to a DB, Connection to API, Logging, etc
'''

class SingleTon(object):
    _instance = None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

o1 = SingleTon('Jaspreet','Sethi')
print(o1)
print(o1.__dict__)
print(o1.fname + o1.lname)
