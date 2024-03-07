#!/usr/bin/python3.4

def intersect(*args):
    first = args[0]
    
    res = []
    for item in first:
        if item in res:
            continue

        for others in args[1:]:
            if item not in others:
                break
        else:
            res.append(item)

    return res


print(intersect('apam','spam','scam','slam')) ##['a', 'm']

print(intersect((1,2,3,4),[4,5,1,0], range(6)))

