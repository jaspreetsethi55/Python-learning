class A:
	print(10)

class B(A):
	print(12)

class C(A):
	print(14)

class D(B,C):  ##B has already inherited A(thus D will also inherit A) and thus print 10, so here C will not inherit A in D since its already inherited via B, so 10 will not get print again
	print(10,12)

o = D()

'''
10

12

14

10 12

'''


class A:
	print(10)

class B(A):
	print(12)

class C(B):
	print(14)

class D(B,C): ##Will work in python2.7 but will give error in python3
	print(10,12)

o = D()

'''
12

14

10 12

Traceback (most recent call last):

  File "<string>", line 14, in <module>

  TypeError: Cannot create a consistent method resolution

  order (MRO) for bases B, C

  > 
'''
