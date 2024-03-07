s = ['geek', 'seek', 'mom']

##Solution 1:
for i in s:
    new = ''
    for j in range(len(i)-1,-1,-1):
        new += i[j]
    if i==new:
        print(i)



##Solution 2:
for i in s:
    if i == s[::-1]:
        print(i)

