l = [3,4,6,90,56,34,89,0]

max,second = l[0],l[0]
for i in range(1,len(l)):
	if l[i] > max:
		second = max
		max = l[i]
	elif l[i] > second and l[i] < max:
		second = l[i]

print(second)
