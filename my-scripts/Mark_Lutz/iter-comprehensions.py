#!/usr/bin/python3.4

'''
####Iterable - Any object that supports 'iter' call is iterable. In general, we can loop around any iterable object. E.g. List,dict, map, zip, range, etc
####Iterator - When we apply 'iter' call to any iterable object then a 'iterator' is returned which supports __next__.object or next(object) call
####iter - iter is a function thet converts itrerable to iterator objects, so we can apply 'next' call on them
####Iteration tool/context - These help us to iterate(loop) around iterable/iterator. E.g. for, comprehension, map,etc

##map, zip, generators, etc are iteration tool as well as iterables
##map,zip,filter, enumerate are iterables as well as iterataors i.e. they are their own iterators(returning themselves for iter() call thus we don't have to neccesarilly use 'iter' on them and instead can directly use 'next'

#Actually technically in backgroud, for/while loop works on iter concept only
#In pyhton 2.x we have X.next() and it Python 3.x we have X.__next__()
#next(X) works in both python 2.x and 3.x and actually internally calls X.next() in 2.X and X.__next__() in 3.X
#when 'next' reaches eof(technically end of any iterator we are applying it on) it gives 'StopIteration' Exception
'''

#######How for loops work in background########
L = [1,2,3]

for i in L: ##for loop internally calls I.__next__()
  pass

I = iter(L)  ##iter internally calls _iter_ method. similar, as next(I) internally calls I.__next__()
I.__next__() #This is 1 
next(I) ##Same as I.__next__() , next(I) internally calls I.__next__()
next(I) #This is 3
#next(I) #This will gives stopIteration exception as there are no more elements left to scan in List L. In for loop this handled automatically(internally) by for loop
          
#Understanding how for loop is implemented using 'iter'
'''This(while loops) will be slower because:
because iterators run at C language speed inside python whereas 'while' loop runs the python byte code via normal python virtual machine
'''
I = iter(L)
while True:
  try:
    x = next(I)
  except StopIteration:
    break
  print(x,end=' ')




#######File handle iter implementation###########

f = open('test.txt')
print(f.readline()) ##Gives first line of file 'test.txt'
print(f.readline()) ##Gives second line of file 'test.txt'
print(f.readline()) ##Returns empty string at eof (but don't give any error)

#Now lets implement above logic via 'iter' and 'next'
f = open('test.txt')
print(f.__next__()) #Please do note that we have not use 'iter' here as file objects are their own iterators, so using iter(f) is not needed, although we can use it
print(f.__next__())
#print(f.__next__()) #This will give stopIteration exception as eof is reached

#proving that file objects are there own iterator
print(iter(f) is f) #True
print(iter(L) is L) #False




#################dict,range 'iter' implementation##########################
d = { 1:'a', 2:'b', 3:'c' }
for key in d: #In python 3.x dictionaries are iterables with an iterator that automatically returns one key at a time
  print(key,d[key])

#how it works
I = iter(d)
next(I) #'a'
next(I) #'b'
next(I) #'c'
#next(I) ## Gives StopIteration Exception


##range
r = range(5)
print(r) #prints range(0, 5)
I = iter(r) ##we can also use I = iter(range(5))
next(I) #0
next(I) #1
next(I) #2
next(I) #3
next(I) #4
#next(I) #Gives stopIteration exception



######map,zip,enumerate and filter 'iter' implementation####################
'''
#All these are their own iterators, thus , we don't need to use 'iter' with them
#map,zip,filter, enumerate are iterables as well as iterataors i.e. they are their own iterators(returning themselves for iter() call thus we don't have to neccesarilly use 'iter' on them and instead can directly use 'next'
'''
#enumerate
l = ['a','b','c']
I = enumerate(l) ##prints <enumerate object at 0x7f1d89f1dc18>
next(I) #(0, 'a')  
next(I) #(1, 'b')  
next(I) #(2, 'c')
#next(I) # this will give stopIteration exception

#we can also apply list function directly to convert any iterable to list
print(list(enumerate(l))) #[(0, 'a'), (1, 'b'), (2, 'c')]

#map
M = map(abs,[-1,0,1])
next(M)
next(M)
next(M)
#next(M) #Gives stopIteration exception

for i in M:
  print(i)  ##This will not print anything as map iterator 'M' is already exhausted above and is thus empty

M = map(abs,[-1,0,1]) ##Again defining it for using it
for i in M:
  print(i)

#filter - filter(func,iterable) - It returns items in an iterable for which passed in function returns true
#filter accepts iterable as well as return iterable

F = filter(bool,['spam','','ni'])
print(F) # <filter object at 0x7f3a4c242d68>
print(list(F)) # ['spam','ni'] 
#next(F) #Gives stopIteration exception as F already got exhausted and empty when we applied 'list' on it. Thus we can only use assigned iterator once



#########################################Comprehensions#######################################
'''
List comprehensions are almost twice as fast as for loop(when used without if condition) because their iterations are performed at C language speed inside the interpreter rather than with manual python code.
List comprehensions are very useful/fast when dealing with large files
'''

lines = [ line.rstrip() for line in open('test.txt') ]

##Printing lines(in list) ending with digit in a file
print( [line.rstrip() for line in open('test.txt') if line.rstrip()[-1].isdigit()] )

##Nested comprehension loops
x = [1,2,3]
y = ['a','b','c']

print([ str(i)+j for i in x for j in y ]) ##['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
#equivalent for loop for above comprehension
res = []
for i in x:
  for j in y:
    res.append(str(i)+j)
print(res)


######################Only 'range' supports multiple iterators as well as iterator indexing, zip/map/filter supports only single scan iterators############
a = map(abs,[-1,0,1])
b = iter(a)
c = iter(a)

next(b) #1
next(c) #0 ##Instead of 1 it gives 0 i.e. starts from index 1 as index 0 was consumed by next(b). this is because map supports only single iterators
next(c) #1
#next(b) 
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  StopIteration
'''
#next(c)
'''
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
'''

##But range supports multiple iterators
a = range(4) #[0,1,2,3]
c = iter(a)
b = iter(a)

next(b) #0
next(c) #0 #Again starts from index 0 because range supports multiple iterators
next(b) #1
next(c) #1

#Multiple iterators returns a new object in place of themselves while single iterators return themselves
