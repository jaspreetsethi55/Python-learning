
L = [1,[[2,4,5],[9],10],[3,4,5],65,55]

def recursive_sum(L):
    sum = 0

    for i in L:
        if(isinstance(i,list)):
            recursive_sum(i)
        else:
            sum += i

    return sum

print(recursive_sum(L))
