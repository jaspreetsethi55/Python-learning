'''
Arrays are fixed-sized continous data records that can be accessed by index number.

###########Features###########
##They are fixed sized
Example: Array[25]

##They are continuos i.e. stored in continuos blocks of memory one after another(size i.e. how many blocks to choose is already fixed above):
end - contains index of last element. If List is empty then end = -1
Intially when Array is mpty and we insert anything in array, it starts inserting from tail(end)


Example: Array[5]
Insert(1) -- in this case start = end = 0

Memory location:  200
Element values:   1
Index:            0

Insert(2) -- in this case start = 0, end = 1
Memory location:  200_201
Element values:   1  | 2 |
Index:            0    1  

...
...
insert(3)
insert(4)
insert(5)
...
...

Final Arrray:
Memory location:  200_201_202_203_204
Element values:   1  | 2 | 3 | 4 | 5|
Index:            0    1   2   3   4

Each element is linked to index which in turn is linked to memory location in cpu.
Index always starts from 0



########Functions########
##Accesssing/Modifying elements: Complexity is O(1) .
Since we know the index(& index knows memory location) associated with the element, we can just access it via index.
E.g. A[1] gives us the 2nd element(since index starts from 0)

##Inserting elements: Complexity is O(n)
insert(val) -- insert at end -- O(1) but if size is of array is full then O(n) coz new_array = old_array + val
insert(pos,val) i.e. insert(0,0) -- O(n)

Time is directly propotional to length of Array.
Let us say, in worst case we want to insert element at beginning of array, then each element needs to get shifted towards right by one position. Thus, n(length) elemnts will get changed/accessed
Example: If we insert 0 starting position in above ARRAY[5]
insert(pos,val) i.e. insert(0,0)
Memory location:  200__201__202__203__204
Element values:   0  | 1  | 2 | 3 | 4 | 5|
Index:            0    1    2   3   4   5

##Deleting elements: Complexity is O(n)
In worst case, let us say we want to delete the first element , then each element needs to be  shifted towards left by one position

##Count elements: Complexity is O(n)

##When Array is Full:
Then a new larger array(technically of double size - although it depends) is created and old array is copy in to this and old array is now free from memory location.
New Array = Old Array + new elements
'''

