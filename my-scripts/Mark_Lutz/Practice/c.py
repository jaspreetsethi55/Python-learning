a = [0,1,2,3]

for i in range(1):
    first = a[-1]

    a[i+1],a[0] = a[i],first

print(a)
