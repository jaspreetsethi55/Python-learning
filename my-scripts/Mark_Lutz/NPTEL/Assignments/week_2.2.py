#!/usr/bin/python3.4

'''
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.


>>> matched("zb%78")
True
>>> matched("(7)(a")
False
>>> matched("a)*(?")
False
>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True

'''

import sys

def matched(s):

    count = 0
    for i in s:
        if(i == '('):
            count +=  1
        elif(i == ')'):
            if(count > 0):
                count -= 1
            else:
                return 'unmatched'

    if(count == 0):
        return 'matched'
    else:
        return 'unmatched'

print(matched(sys.argv[1]))
