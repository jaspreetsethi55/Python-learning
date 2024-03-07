#!/user/bin/python3.4

names_1 = ['jaspreet', 'vinod', 'shobit', 'seth', '']
names_2 = ['jaspreet', 'vinod', 'shobit', 'seth']
names_3 = []

##For-else Loop##
##If break is encountered i.e. break condition is true aand break statement is executed then 'else' will not work
##If break is not encountered i.e. break condition is not true and break statement is not executed then 'else' will be executed & will hv last executed value(i) of loop##If for loop is not executed then else is directly executed

##If break is encountered i.e. break condition is true aand break statement is executed then 'else' will not work
for i in names_1:
    print(i,end=' ')
    if not i:
        print("\nUndefined name found:",i)
        break ##break statement will be executed as '' in names_1 is undefined and thus 'else' will not be called
else:
    print("all names are defined:names_1")

'''
output:
jaspreet vinod shobit seth
Undefined name found:
'''


##If break is not encountered i.e. break condition is not true and break statement is not executed then 'else' will be executed & will hv last executed value(i) of loop
for i in names_2:
    print(i,end=' ')
    if not i:
        print("\nUndefined name found:",i)
        break
else:
    print("\nall names are defined:names_2") ##'else' will be executed as break is not executed

'''
output:
jaspreet vinod shobit seth
all names are defined:names_2
'''


##If for loop is not executed then else is directly executed
for i in names_3:
    print(i,end=' ')
    break
else:
    print("No name is defined:names_3")


'''
output:
No name is defined:names_3
'''



#############While-else loop works in the same way as for-else loop(same condition as stated above#############
i = 0
while i < len(names_1):
    print(names_1[i],end=' ')
    if not names_1[i]:
        print("\nUndefined name found at index:",i)
        break
    i+=1
else:
    print("TEST:all names are defined")

'''
output:
jaspreet vinod shobit seth 
Undefined name found at index: 4
'''




####Unpacking nested sequences  -   Multiple variable assignments within for loop using tuples
num = [ [1,2,3], [3,4,5], [4,5,6] ]

for (x,y,z) in num:
    print(x,y,z)

'''
output:
1 2 3
3 4 5
4 5 6
'''

((a,b),c) = ((1,2),3)
print(a,b,c)

'''
output
1 2 3
'''

for((a,b),c) in [ ((1,2),3) , ((4,5),6) ]:
    print(a,b,c)

'''
output:
1 2 3
4 5 6
'''

for((a,b),c) in [ ((1,2),3) , ('xy',6) ]:  ##This is a good example of unpacking
    print(a,b,c)

'''
output:
1 2 3
x y 6
'''

##Extended sequence assignment - Assigning multiple elements to single element using *  - *variable will store items as list
for (a,*b,c) in [(1,2,3,4), [5,6,7,8]]: ##Asignment is quite generic, works in same way for different sequences. E.g. one element is tuple and and other is list 
    print(a,b,c)

'''
output:
1 [2,3] 4
5 [6,7] 8
'''

##Fastest way to open file to read
for line in open('test.txt'): ##works on iterator concept(calling next func automatically) and don't load file in to memory
    print(line.rstrip())





'''
Range Function: range(start,end,interval)
returns a iterable object
range(5) - gives numbers 0 to 4 (not 5)
range(-5,5) - gives numbers -5 to 4
range(4,10,2) - gives 4,6,8
'''

######shuffling/re-ordering sequence
l = [1,2,3]
for i in range(len(l)):
    x = l[i:] + l[:i]
    print(x, end=' ')
print()

'''
output:
[1,2,3] [2,3,1] [3,1,2]
'''

######Getting every second element of sequence
l = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(l),2):
    print(l[i], end=' ')
print()

'''
output:
1 3 5 7 9
'''

for i in l[::2]: ##Best way to get any nth consecutive element 
  print(i,end=' ')
print()

'''
output:
1 3 5 7 9
'''



'''
zip: allow us to parallel traverse sequences
In case one sequence is smaller, zip ignores extra elements of larger sequence
zip returns an iterable object and we can use 'list' function to convert it to list
'''

a = 'xyz'
b = 'abc'
print(list(zip(a,b)))  ##returns a list of tuples

'''
output:
[('x', 'a'), ('y', 'b'), ('z', 'c')]
'''

m = [1,2,3,4]
n = [1,2,3]
for i in zip(m,n):
    print(i,end=' ')
print()

'''
output:
(1,1) (2,2) (3,3)
'''




'''
enumerate: we can use this with any iterable object and it returns a generator function and when we use next on this generator function it returns a tuple with offset and value(one by one of iterable object)
'''
a = 'abc'
E = enumerate(a)

print(E)
print(next(E))
print(next(E))

for (i,v) in enumerate(a):
    print(i,v)


