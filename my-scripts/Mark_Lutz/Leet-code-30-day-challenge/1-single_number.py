'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


'''
Solution Logic:
The best solution is to use XOR. XOR of all array elements gives us the number with single occurrence. The idea is based on following two facts.
a) XOR of a number with itself is 0.
b) XOR of a number with 0 is number itself.

Let us consider the above example.  
Let ^ be xor operator as in C and C++.

res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

Since XOR is associative and commutative, above 
expression can be written as:
res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
    = 7 ^ 0 ^ 0 ^ 0
    = 7 ^ 0
    = 7 
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(1,len(nums)):
            res = res ^ nums[i]

        return res
