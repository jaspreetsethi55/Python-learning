import numpy as np
#####Arithmetic operations
'''
addition(+):

subtraction(-):

multiplycation(*):

divide(/):

how operations happens:
1. Operation on single array with some value/function:
a operator 4:
E.g. a + 4  - will add 4 to each element

2. Operation on multiple arrays:
In numpy, these operations are element-wise i.e. operations are applied only between corresponding elements, namely that occupy same position.
a aperator b . E.g. a + b - will add each corresponding element of a to b. size of a & b should be same
E.g. a * np.sqrt(b)
'''

a = np.arange(4)
print(a) #[0 1 2 3]
print(a+4) #[4 5 6 7]

a = np.arange(1,4) #[1 2 3]
b = np.arange(4,7) #[4 5 6]
print(a+b) #[5 7 9]
print(a-b) #[-3 -3 -3]
print(a*b) #[4 10 13]

print(a * np.sin(b)) #[-0.7568025  -1.91784855 -0.83824649]
print(a * np.sqrt(b)) #[2.         4.47213595 7.34846923]


A = np.arange(0,9).reshape(3,3)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

#B = np.ones((3,3))
B = np.arange(0,9).reshape(3,3)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''
print(A + B)
'''
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
'''


print("dot")
print(np.dot(A,B))
#############matrix product
'''
dot() function is use to calculate matrix product.
The result at each position, is the sum of products between each element of the corresponding row of the first matrix with corresponding element of the corresponding column of the second matrix.

syntax: np.dot(A,B) or A.dot(B)

Example: np.dot(A,B)
[[ 3.  3.  3.]
 [12. 12. 12.]
 [21. 21. 21.]]

calculation:
    A            B
[[0 1 2]     [[1. 1. 1.],
 [3 4 5]      [1. 1. 1.],
 [6 7 8]]     [1. 1. 1.]]

1st row of A
0 1 2 
      1  1st column of B
      1
      1
0*1 + 1*1 + 2*1 = 3

2nd row of A
3 4 5 
      1 2nd column of B
      1
      1
3*1 + 4*1 + 5*1 = 12

3rd row of A
6 7 8
      1 3rd column of B
      1
      1
6*1 + 7*1 + 8*1 = 21


Also, do note that np.dot(A,B) anf np.dot(B,A) will have different results
'''


######increment & decrement operators
'''
+= -- For increasing
-= -- For decreasing
*= -- Fo multiplying

This applies on each element of the numpy array
'''

a = np.arange(4) # [ 0 1 2 3 ]
a += 1  # [ 1 2 3 4 ]


######Universal Functions(ufunc)
'''
ufunc is a function that acts individually on each single element of the input array to generate a corresponding result in new output array.

some ufunc are sqrt(), log(), sin(), etc

E.g. np.sqrt(a)
'''

a = np.arange(4) #[1 2 3 4]
print(np.sqrt(a)) #[0.         1.         1.41421356 1.73205081]


#######Aggregate Functions
'''
Aggregate functions are those functions that perform an operation on a set of values, an array for example and produce a ingle result.

sum(), min(), max(), mean(), std()
'''
a = np.arange(1,5) #[1 2 3 4]
print(a.sum()) #10
print(a.mean()) #2.5


######Indexing, Slicing and Iterating
'''
###Accessing:
a = np.range(1,5) #[1 2 3 4]
a[0] -- 1
a[3] -- 4
a[-1] -- 4
a[[1,3]] -- [2 4]

A = np.arange(10,19).reshape((3,3))
print(A)
[[10 11 12]
 [13 14 15]
 [16 17 18]]

A[1,2] -- 15 -- 1+1(2nd) row of 2+1(3rd) column as index starts from 0


###Slicing:
extracting portion of an array.
Arrays obtained by slicing are views on same underlying buffer i.e. modifying sliced array will actually modify the orginial array too.
syntax: a[start:end:n] -- start to end-1 by skipping each n-1 element

a = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
b = a[0:5]
b[0] = 8
print(a) #[8 1 2 3 4 5 6 7 8 9]
print(b) #[8 1 2 3 4]

a = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
print(a[1:8:2]) #[1 3 5 7]
print(a[::2]) #[0 2 4 6 8] -- every 2nd element
print(a[:5:]) #[0 1 2 3 4]

A = np.arange(10,19).reshape((3,3))
print(A)
[[10 11 12]
 [13 14 15]
 [16 17 18]]

print(A[0,:]) #[10 11 12]
print(A[:,0] #[10 13 16]
print(A[0:2,0:2])
[[10 11],
 [13 14]]

print(A[[0,2],0:2]) ## 0 & 1 column of 0th and 2nd row
[[10 11]
 [16 17]]

'''
