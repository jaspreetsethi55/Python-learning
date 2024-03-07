import re

def findallstr(s):
    res = ','.join( map(lambda x:x.group(), re.finditer(r'[aeiou]{2,}',s,re.IGNORECASE)) )

    if ',' in res:
        for i in res.split(','):
            print(i)
    else:
        print(-1)
#findallstr('match a single character not present in the list below')
findallstr('rabcdeefgyYhFjkIoomnpOeorteeeeet')
