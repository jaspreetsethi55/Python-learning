##Making our own reduce function, which we work exactly the same way, python reduce functions works

l =[1,2,3,4,5]

##python reduce function
from functools import reduce
res = reduce((lambda x,y:x+y),l)
print(res) ##15


##Making our own reduce function
def myreduce(func,seq):
    res,*rest = seq

    for i in rest:
        res = func(res,i)
    return res

res = myreduce((lambda x,y:x+y),l)
print(res)  ##15


