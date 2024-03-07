s='defjjhaaaprforifbrgbfaaaaaaaa'

d = {}
max_key=s[0]
for i in s:
    d[i] = d.get(i,0) + 1

    if( d[max_key] < d[i]):
        max_key = i

print(max_key) 

