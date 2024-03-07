'''
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right. For instance, given the array ,  is between two subarrays that sum to . If your starting array is , that element satisfies the rule as left and right sum to .

You will be given arrays of integers and must determine whether there is an element that meets the criterion.

Function Description
Complete the balance
dSums function in the editor below. It should return a string, either YES if there is an element meeting the criterion or NO otherwise.

balancedSums has the following parameter(s):
arr: an array of integers
'''

l = [1,1,4,1,1]

# Complete the balancedSums function below.
def balancedSums(arr,n): #1 1 4 1 1
    left,right = 0,0

    if n == 1:
        return "Yes"

    for i in range(n):
 
        left = 0 if i == 0 else sum(arr[0:i])
        right = 0 if i == n-1 else sum(arr[i+1:])

        print(left,right)
        if left == right:
            return "Yes"
    else:
        return "No"

balancedSums(l,5)

