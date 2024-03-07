'''
Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 

    Input: 19
Output: true
Explanation: 
    12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

'''
Solution:
The solution is fairly simple, when the total sums to a single digit, then you
need to check the end result.
If you list the values in an excel, its super easy to see the math behind it.
I'll list my table here (read vertically).

4   5   7   9
16  25  49  81
37  29  97  65
58  85  130 61
89  89  10  37
145 --  1   58
42  --  --  89
20  --  --  --
4   --  --  --
As you can see, only 1 and 7 actualy goes to 1, all the others esentially go to
the result from 2. In another word, all numbers 2, 4, 6, 8 (multiply of 2) and
3, 9 (multiply of 3) essentially goes to number 89, which then goes back to
4 and loop over again. Thus our end condition is 1 or 7.
'''


class Solution:
    def isHappy(self, n: int) -> bool:       
        sum = 0
        for i in str(n):
            sum += int(i)*int(i)

        if sum == 1 or sum == 7:
            return True
        else:
            if sum < 10:
                return False
            else:
                return self.isHappy(sum)
