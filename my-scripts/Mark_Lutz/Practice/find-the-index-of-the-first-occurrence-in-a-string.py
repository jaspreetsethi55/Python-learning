'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''


##Solution-1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len, needle_len = len(haystack), len(needle)
        for i in range(haystack_len):
            #check if length of haystack[i:] is greater then or equal needle length else we will get index out of range error
            #if len(haystack[i:]) >= needle_len and haystack[i:i+needle_len] == needle:
            if haystack[i:i+needle_len] == needle: #we don't get index out of range error with multiple index a[i:len+1]
                return i

        return -1
