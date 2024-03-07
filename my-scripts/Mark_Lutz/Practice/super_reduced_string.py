'''
Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String

Function Description

Complete the superReducedString function in the editor below. It should return the super reduced string or Empty String if the final string is empty.

superReducedString has the following parameter(s):

s: a string to reduce
Input Format

A single string, .

Constraints

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd
Sample Output 0

abd
Explanation 0

Steve performs the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd
Sample Input 1

aa
Sample Output 1

Empty String
Explanation 1

aa → Empty String
Sample Input 2

baab
Sample Output 2

Empty String
Explanation 2

baab → bb → Empty String
'''

def reduce_string(s):
    l = list(s)
    

    i=1
    while( i < len(l)):
        print(i,l[i],l)
        if l[i] == l[i-1]:
            del l[i-1:i+1]
            i=i-1
            print('Inside',i,l)
            continue

        i=i+1
    
    if len(l) == 2 and l[0] == l[1]:
        return 'Empty String'
    if len(l)>0:
        return ''.join(l)
    else:
        return 'Empty String'
       
      
#print(reduce_string('aaabccddd'))
#print(reduce_string('a'))
#print(reduce_string('aa'))
#print(reduce_string('baab'))


def reduce_str(s):
    if (len(s) == 2 and s[0] == s[1]) or not s:
        return 'Empty String'

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            reduce_str(s[:i-1]+s[i+1:])
            continue
    
    return s

#print(reduce_str('aaabccddd'))
def super_reduced_string(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return ''.join(stack)  
    else:
        return 'Empty String'

print(super_reduced_string('aaabccddd'))
print(super_reduced_string('aaa'))
print(super_reduced_string('a'))
print(super_reduced_string('aa'))
