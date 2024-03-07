L1 = [1,2,3]
L2 = [5,6,7]
L3 = [8,9,10]

for x,y,z in [ [i,j,k] for i in L1
        for j in L2
        for k in L3 ]:
    print(x,y,z)
