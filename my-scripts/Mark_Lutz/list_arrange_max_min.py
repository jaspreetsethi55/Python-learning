l = [1,4,5,9,10,33,22,6,10]

new_list = []
for i in range(len(l)):
    min,max = i,i
    for j in range(i+1,len(l)):
        if l[j] > l[max]:
            max = j
        if l[j] < l[min]:
            min = j
    new_list.append(max)
    new_list.append(min)
print(new_list)


