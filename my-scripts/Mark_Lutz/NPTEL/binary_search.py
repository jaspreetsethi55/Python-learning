#!/usr/bin/python3.4

class Tree:
    def __init__(self,initial_val = None):
        self.value = initial_val

        if(self.value):
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

        return()

    def is_empty(self):
        return(self.value == None)

    def in_order_traverse(self):
        if(self.empty):
            return([])
        else:
            return(self.left.in_order_traverse() + [self.value] + self.right.in_order_traverse())

     def __str__(self):
        return(str(self.in_order_traverse()))




