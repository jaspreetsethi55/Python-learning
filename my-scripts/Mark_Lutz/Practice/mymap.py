##Making our own map generator function, which we work exactly the same way, python map functions works

l =[1,2,3,4,5]

##python map function
res = map((lambda x:x**2),l)
print(list(res)) ##[1, 4, 9, 16, 25]


##Making our own map function/generator
def mymap(func,seq):
    for _ in seq:
        res = func(_)
        yield res


res = mymap((lambda x:x**2),l)
print(list(res))  ##[1, 4, 9, 16, 25]


##Making our own map function/generator
def mymap(func,seq):
    return ( func(x) for x in seq)


res = mymap((lambda x:x**2),l)
print(list(res))  ##[1, 4, 9, 16, 25]
