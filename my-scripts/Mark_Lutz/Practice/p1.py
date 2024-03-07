s = ['geek', 'seek', 'mom']

for element in s:
    if element == element[::-1]:
        print("{} is palindrome".format(element))
