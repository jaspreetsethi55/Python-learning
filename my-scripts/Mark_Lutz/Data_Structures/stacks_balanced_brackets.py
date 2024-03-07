def balanced(s):
    brackets = dict(zip(('(','{','[','*'),(')','}',']','*')))
    stack = []

    for i in s:
        ##If open bracket i.e. (,{ or [ then append in stack
        if i in brackets:
            stack.append(i)

        ##If closed bracket    
        else:
            ##If stack is empty i.e. string may start(at beginning or mid) with close bracket E.g. '}' , '{}}[{}]
            #or
            ## Closed bracket (,{ or [ must match with last inserted open bracket i.e. pair matching
            if stack == [] or i != brackets[stack[-1]]: 
                return 'Not Matched:{}'.format(stack)

            ##If pair matched , then deleting/pop the last open bracket
            else:
                stack.pop()

    if stack == []:
        return 'Matched'
    else:
        return 'Not Matched:{}'.format(stack)

#a = '[{}{}{()}{{{}}}(])'
#b = '[{}{}{()}{{{}}}]'
#c = '{}}[{}{}{()}{{{}}}]'

a = "()"
b = "(*)"
c = "(*))"
print(balanced(a))
print(balanced(b))
print(balanced(c))
