print("********Declaring Dictionaries********")

first_dict = { 'a':1, 'b':2, 'c':3, 'd':4 }
print("first_dict = ",first_dict,end='\n\n')

first_dict = dict(a=1, b=2, c=3, d=4 ) ## Don't give keys is single bracket when using dict else we'll get keyword-expression syntax error. dict('a'=1) will give error
print("Don't give keys in single quotes when using simple brackets with 'dict' function else we'll get keyword-expression syntax error. dict('a'=1) will give error");
print("first_dict = dict(a=1, b=2, c=3, d=4 )\n",first_dict,end='\n\n')

first_dict = dict([('a',1) , ('b',2), ('c',3), ('d',4)])
print("first_dict = dict([('a',1) , ('b',2), ('c',3), ('d',4)])\n",first_dict,end='\n\n')

f_keys = ['a','b','c','d']
f_values = [1,2,3,4]
first_dict = dict(zip(f_keys,f_values))
print('''
f_keys = ['a','b','c','d']
f_values = [1,2,3,4]
first_dict = dict(zip(f_keys,f_values))''',"\n",
first_dict,end='\n\n\n')


print("**********Accessing Dictionary values********")
print("first_dict[a] = ",first_dict['a'],end='\n\n')

print("first_dict.keys()\n",first_dict.keys(),end='\n\n')
print("first_dict.values()\n",first_dict.values(),end='\n\n')
print("first_dict.items()\n",first_dict.items(),end='\n\n')

print("By Default in Pyhton 3.3 key/value/item function return iterables/view and not list. We can use 'list' function to convert them to list\n")
keys_list = list(first_dict.keys())
print("keys_list = list(first_dict.keys())\nkeys_list\n",keys_list,end='\n\n')

print("first_dict.get('a')\n",first_dict.get('a'),end='\n\n')
print("first_dict.get('e')\n",first_dict.get('e'),end='\n\n')
print("first_dict.get('e',5)\n",first_dict.get('e',5),end='\n\n')


print("**********Modifying/Adding/Deleting Dictionary**********")
first_dict['e'] = 5
print("#Adding:\nfirst_dict['e'] = 5\n",first_dict,end='\n\n')

first_dict['b'] = 6
print("#Modifying:\nfirst_dict['b'] = 6\nfirst_dict = ",first_dict,end='\n\n')

del_value = first_dict.pop('c')
print("Deleting:\ndel_value = first_dict.pop('c')\nfirst_dict = ",first_dict,end='\n')
print("Deleted Value is del_value:", del_value,end='\n\n')

del_val = first_dict.pop('x',10)
print("Deleting non-defined key:\ndel_val = first_dict.pop('x', 10)\nfirst_dict = ",first_dict,end='\n')
print("Nothing Deleted from first_dict but default value(as was  passed) is return:", del_val,end='\n\n')

del first_dict['b']
print("Deleting:\ndel first_dict['b']\nfirst_dict = ",first_dict,end='\n\n')


print("**********Looping*************")
print('''
for i in first_dict.keys():
	print(i,':',first_dict[i])
''')
for i in first_dict.keys():
        print(i,':',first_dict[i])

print('''
##By default dictionary in loop return keys, so first_dict.keys() and first_dict means same while looping
for i in first_dict:
	print(i,':',first_dict[i])
''')
for i in first_dict:
        print(i,':',first_dict[i])


print('''
#Values:
for val in first_dict.values():
        print(val)
''')
for val in first_dict.values():
        print(val)

print('''
#Items:
for val in first_dict.items():
        print(val)
''')
for key,val in first_dict.items():
        print(key,':',val)


print("*******Dictionary Comprehension**********")

print('''
dict_sq = { key:key*2 for key in first_dict }''')
dict_sq = { key:key*2 for key in first_dict }
print(dict_sq)
