num = [1,2,3,4]
alph = list('abcd')
range_list = list(range(-4,10,2))

print("******Declaring Lists******")
print("List declared by using []:")
print(num,end='\n\n')

print("List declared by using list function:list('abcd')")
print(alph,end='\n\n')

print("List declared by using range function:list(range(-4,10,2)")
print(range_list,end='\n\n')




 
print("******Accessing Lists******")
print(num)
print("num[0]:",num[0])
print("num[0:1]:",num[0:1])

print("num[0:2]",num[0:2])
print("num[:2]",num[:2])
print("num[1:]",num[1:])

print("num[-1]:",num[-1])
print("num[-1:0]:",num[-1:0])
print("num[-1:]:",num[-1:])
print("num[0:-1]:",num[0:-1],end='\n\n')




print("******Modifying Lists******")
print("num=",num)

num[1] = 1
print("num[1] = 1 --",num)

num[1:3] = [5,6,7]
print("num[1:3] = [5,6,7] --", num)

num[2:4] = num[3:5]
print("num[2:4] = num[3:5] -- ",num)

##num[0:0] = 0 - This will give error
num[0:0] = [0]
print("num[0:0] = 0 -- ",num,"#Inerting at beginning",end='\n\n')



print("******Concatenating List******")
num = num + [8,9,10]
print("num = num + [8,9,10] --",num,end='\n\n')



print("******List Functions******")
print("num=",num)
num.append("last")
print("num.append('last') --",num)

num.extend(['x','y','z'])
print("num.extend(['x','y','z'])--",num)

num.insert(3,'j')
print("num.insert(3,'j')--",num)

num.pop()
print("num.pop()--",num)

num.remove(5)
print("num.remove(5)--",num)

del num[2]
print("del num[2]--",num)

index = num.index('x')
print("num.index('x')--",index)

count = num.count(4)
print("num.count(4)--",count)


print("******For Loop******")
print("""
new_num = []
for i in num:
        if i == 0:
                i = str(i) * 4
        new_num.append(i)
""")

new_num = []
for i in num:
	if i == 0:
		i = str(i) * 4
	new_num.append(i)

print(new_num)

print("""
new_num = []
for i in num:
        if i == 0:
                i = [i] * 4
        new_num.append(i)
""")

new_num = []
for i in num:
        if i == 0:
                i = [i] * 4
        new_num.append(i)

print(new_num)


print("******Comprehensions******")
print("""#Now doing same stuff by comprehensions
new_num = [str(i)*4 if i == 0 else i for i in num]""")
new_num = [str(i)*4 if i == 0 else i for i in num]
print(new_num) 

print("""
new_num = [[i]*4 if i == 0 else i for i in num]""")
new_num = [[i]*4 if i == 0 else i for i in num]
print(new_num)

print("""##If only If condition is there then it should be declared after for loop
new_num = [i for i in num if type(i) is int]""")
new_num = [i for i in num if type(i) is int]
print(new_num,end='\n\n')



print("*********map function********") 
print("new_num = list(map(abs,[1,-1,0,0,1,-2]))")
new_num = list(map(abs,[1,-1,0,0,1,-2]))
print(new_num, end='\n\n')


print("*******Sorting List******")
print("""
num_sort = num.sort()
This will give error because in Python 3 mixed type(E.g. int and str) raises exception
""")
print("num =",end=' ')
print(num)

print("""
num_sort = num.sort(key=str) ##num.sort(key=str,reverse=True) for descending/reverse order
print(num_sort) ##this returns nothing as sort returns 'None' and change the original list
print(num) # this will be now sorted
""")

num_sort = num.sort(key=str)
print(num_sort)
print(num)

print("""
num_sort = sorted(num,key=str,reverse=True) ## this will not modify orignal list(as num.sort does) and reurns sorted list
print(num_sort)
print(num)
""")

num_sort = sorted(num,key=str,reverse=True)
print(num_sort)
print(num)
