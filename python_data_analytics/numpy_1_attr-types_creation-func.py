################numpy###########
'''
Knowledge of numpy is neccessary and kind of prerequisite in order to learn other scientific packages, specially pandas library.

In 1995, Jim Hugunin, came up with package 'Numeric' which was sucessfully followed by an alternative package known as 'Numarray'. This ambiguity led to idea of unifying these 2 packages & then Travis Oliphant came up with 'Numpy' library.

Currently Numpy is open sourced and licensed under BSD
'''

####Numpy installation
'''
Ubuntu: sudo apt-get install python-numpy
Fedora: sudo yum install numpy scipy
Windows(Ananconda): conda install numpy
'''

import numpy as np

####Ndarray: heart of numpy Library
'''
Numpy array size are fixed i.e. once we define at the time of creation, we cannot change it.

Ndarray:
Each numpy array is of type/object 'Ndarray' i.e. Ndarray is a multidimensional homogeneous(coz virtually all items within it are of same type and size) array with a predetermined number of items.

dtype:
data type of numpy array

shape:
dimensions and items in an array. A tuple of N positive integers that specifies the size for each dimension.
E.g.(4,3) where 4 is dimension(length of outermost array i.e. total 4 arrays are defined) and 3 is length of each array

axes & rank:
dimensions are defined as axes and number of axes as rank.
'ndim' attribute is used to get axis

size:
array size i.e. total number of elements in ndarray.

itemsize:
size in bytes of each item in array.

data:
buffer containing the actual elements of the array.

creating an array(array() function):
easiest function to define a new array.
E.g. np.array([[1,2,3],[3,4,5]])
Also, sequences of tuples and lists interconnected make no difference.
E.g. np.array([[1,2,3],[3,4,5]]) and np.array([(1,2,3),(3,4,5)])

'''

a = np.array([1,2,3]) #single dimensional

b = np.array([[1,2,3], #multi dimensional - 2 dimensional
             [4,5,6],
             [7,8,9]])

b1 = np.array([[1,2], #multi dimensional - 2 dimensional
             [4,5,6],
             [7,8,9]])

c = np.array([[1.1,2.1,3.1], #multi dimensional - 2 dimensional
             [4.2,5.1,6.3],
             [7.1,8.4,9.8],
             [10.1,11.2,12.3]])

d = np.array([[ [1,2], [3,4]],    #multi dimensional - 3 dimensional
              [ [5,6], [7,8]] ])

print(type(a)) #<class 'numpy.ndarray'>
print(type(b)) #<class 'numpy.ndarray'>


print(a.dtype) ##int64
print(b.dtype) ##int64
print(c.dtype) ##float64


print(a.shape) #(3,) or (3,1) -both are samething ##length of array is 3
print(b.shape) #(3,3) 
print(b1.shape) #(3,) ##For numpy, length of each arrays should be same, since that is not the case here so, we are not getting (3,) in stead of (3,3)
print(c.shape) #(4,3) ##length of array is 4 and each array size is 3
print(d.shape) #(2,2,2)

print(a.ndim) #1 so rank is 1
print(b.ndim) #2 so rank is 2
print(b1.ndim) #1 so rank is 1  ##For numpy, length of each internal array should be same. Here it will become one-dimensional array that stores references to lists, which                                ##means that you will lose most of the benefits of Numpy (vector processing, locality, slicing, etc.).
print(c.ndim) #2 so rank is 2
print(d.ndim) #3 so rank is 3

print(a.size) #3
print(b.size) #9
print(c.size) #12
print(d.size) #8


print(a.itemsize) #8 i.e. 8 bytes
print(b.itemsize) #8 
print(c.itemsize) #8
print(d.itemsize) #8

print(a.data) #<memory at 0x7f4636fd1c80>
print(b.data) #<memory at 0x7f463aa89210>
print(c.data) #<memory at 0x7f463aa89210>
print(d.data) #<memory at 0x7f4636f7e450>



######dtype Option:
'''
We can explicitly define the dtype of array() by using 'dtype' option.
'''

f = np.array([[1,2,3], [4,5,6]], dtype = complex)
print(f)
'''
output:
[[1.+0.j 2.+0.j 3.+0.j]
 [4.+0.j 5.+0.j 6.+0.j]]
'''


######Generating arrays with initial contents:
'''
zeros():
will create full numpy array of zeros with dimensions defined by shape argument.
default dtype is float64. E.g. np.zeroes((3,3))

ones():
will create full numpy array of one's with dimensions defined by shape argument.
default dtype is float64. E.g. np.ones((3,3))
E.g. np.ones((3,3), dtype = "int64")

arange():
generate numpy arrays with numerical sequences based on the passed arguments.
Similar to range function.
syntax: np.arange(start,end,interval) -- will generate numpy array from start to end-1 with desired interval(interval can also be float)
E.g. np.arange(0,10)

reshape():
Divides a linear array in to different parts based on arguments passed.
syntax: reshape(rows, columns)
E.g. a.reshape(3,4) - with divide array a in to 3 rows and 4 columns
We can use this with arange() function to generate multidimensional arrays.
Will give error if array size is smaller then the dimensions specified. E.g. a = np.array[1,2,3], a.reshape(3,3)

linspace():
syntax: linspace(start,end,num_of_elements)
similar to arange but instead of interval, 3rd argument defines the number of elements in which we want the interval to split.
E.g. np.linspace(0,10,5) -- [ 0.   2.5  5.   7.5 10. ]

random():
random() function of numpy.random module.
This will generate random array with number of elements as specified in argument.
E.g. np.random.random(3)  -- [0.45525291 0.90483562 0.57916089]
np.random.random((3,3))
'''

zeroes = np.zeros((3,3))
print(zeroes)
''''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

zeroes = np.zeros((3,3), dtype = "int64")
print(zeroes)
''''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
'''


ones = np.ones((3,3))
print(ones)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''

a = np.arange(0,9)
print(a) ##[0 1 2 3 4 5 6 7 8]

a = np.arange(0,9,3)
print(a) ##[0 3 6]

a = np.arange(0,5,.6)
print(a) #[0.  0.6 1.2 1.8 2.4 3.  3.6 4.2 4.8]

a = np.arange(0,9).reshape(3,3)
print(a)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

a = np.linspace(0,10,5)
print(a) #[ 0.   2.5  5.   7.5 10. ]

a = np.random.random(3)
print(a) #[0.45525291 0.90483562 0.57916089]

a = np.random.random((3,3))
print(a)
'''
[[0.9090569  0.77058137 0.34565341]
 [0.7969043  0.80062625 0.95076565]
 [0.29447796 0.80668382 0.66517464]]
'''
