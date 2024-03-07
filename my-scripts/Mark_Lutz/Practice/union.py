#!/usr/bin/python3.4

def union(*arg):
    res = []
    for items in arg:
        for i in items:
            if i not in res:
                res.append(i)

    return res

        
print(union('apam','spam','slam'))


