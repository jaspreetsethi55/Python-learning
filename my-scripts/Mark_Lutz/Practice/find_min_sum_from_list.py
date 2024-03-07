l = [1,6,9,4,2,5]

min_sum = l[0] + l[1]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        curr_sum = l[i]+l[j]
        if( curr_sum < min_sum):
            min_sum = curr_sum

print(min_sum)

print(min([l[i]+l[j] for i in range(len(l)-1) for j in range(i+1,len(l))]))
