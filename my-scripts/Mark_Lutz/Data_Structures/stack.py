
class Stack:
    '''
    Stack(Last In First out - push(insert)/pop(remove))
    Let us say we have 4 books A,B,C,D lying all over the Floor. Now let's arrange them in stack i.e. First A, then B and so on:

    D
    C
    B
    A

    Now, Since D is in top, so that's the first book we can pick up(while D was kept at end when arranging books). So this is "Last In First Out"
    If we want to take Book B, then first we have to remove books D & C, then we can pick B.

    We use 'Push' while arranging book and 'Pop' while getting the books

    Arranging(push - inserting at end):
    Thus, w.r.t. python, we are having 4 items: A,B,C,D. Arranging these in stack, we need to use push(i.e. append)
    [A] -- push A
    [A,B] -- push B
    [A,B,C] -- push C
    [A,B,C,D] -- push D

    Selecting(pop - deleting from end):
    D -- pop()
    C -- pop()
    B -- pop()
    A -- pop()
    '''

    ##initiallizing Stack
    def __init__(self):
        self.items = []

    ##Insert Item at end
    def push(self,item):
        self.items.append(item)

    ##remove item from end
    def pop(self):
        self.items.pop()

    ##Print Stack
    def get_stack(self):
        print(self.items)

    ##Check is Stack is empty
    def is_empty(self):
        return self.items == []

    ##Getting top(last) item
    def peek(self):
        return self.items[-1]

if __name__ == '__main__':
    print(Stack.__doc__)

    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.get_stack()

    stack.push('C')
    stack.get_stack()

    stack.pop()
    stack.get_stack()



