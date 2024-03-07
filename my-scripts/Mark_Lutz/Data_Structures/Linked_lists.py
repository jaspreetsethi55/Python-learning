'''
#####Linked List######
As the name suggests, a list that is linked together by some mean i.e. seperate nodes are linked together as each node stores its data/value and address of next node.
Each Node has 2 components: data & next
Start/First/current node is known as Head. 
As we traverse along the List, Head Node will move i.e. it will be always the current node i.e. where we currently are.
Last notion is Linked List always null, that helps us figures out that List has come to an end.Similar to 'None' in Python.

___Head____                               __end__
 (A,next)----->(B,next)----->(C,next)----> null
   Node          Node          Node 


Operation:                      Array      Linked-List  Reason
Insertion/Deletion              O(n)        O(1)        With Linked-List,just need to change the pointer 'next' to position at right node
Accesing/Modifying Element      O(1)        O(n)        With linked-list,E.g. for accessing last node, need to go over all nodes via 'next'

Feature:                        Array       Linked-List
Contiguous Memory               Yes         No



Insertion:
**append:
Add element at back of List(append 'D' at end)
___Head____                                           __end__
 (A,next)----->(B,next)----->(C,next)---->(D,next)---> null
   Node          Node          Node         Node

**prepend:
Add element in front of List(prepend 'E' at start)

 ___Head____                                           __end__
   (E,next)--->(A,next)----->(B,next)----->(C,next)---->(D,next)---> null
   Node          Node          Node         Node          Node

**insert_after_node
Add element in between List(insert 'F' between A and B)

 ___Head____                                           __end__
   (E,next)--->(A,next)----->(F,next)----->(B,next)----->(C,next)---->(D,next)---> null
   Node          Node          Node         Node          Node          Node
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    ##Inserting at end
    def append(self,data):
        new_node = Node(data)

        '''If list is empty i.e. head is not pointing anywhere'''
        if self.head is None:
            self.head = new_node
            #print(new_node.__dict__i) #{'next': None, 'data': 'A'}
            #print(self.__dict__) #{'head': <__main__.Node object at 0x7fc5684a2198>} 
            return

        '''If list is not empty, then move head to last position, coz if list is not empty then we need to append at last position'''

        last_node = self.head
        #while next pointer of our current node(last_node) is not pointing to null(None) position
        while last_node.next:
            #Moving head pointer to right
            last_node = last_node.next

        last_node.next = new_node

    ##Inserting at beginning
    def prepend(self,data):
        new_node = Node(data)

        '''If list is empty i.e. head is not pointing anywhere'''
        if self.head is None:
            self.head = new_node
            return
        
        '''
        ##saving our current head/first node
        old_first_node = self.head

        #changing head node to new node
        self.head = new_node
        #head node now points to old first node
        self.head.next = old_first_node  ##or new_node.next = old_first_node
        '''

        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    
llist = LinkedList()
llist.append('A')
llist.print_list()

print('-------------')

llist.append('B')
llist.print_list()
        
print('-------------')

llist.prepend('C')
llist.print_list()
