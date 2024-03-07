###Plaindrome Number####
num = 1221

def palindrome(n):
    if n == int(str(n)[::-1]):
        return 'Palindrome'
    else:
        return 'Not Palindrome'

print(palindrome(num))


