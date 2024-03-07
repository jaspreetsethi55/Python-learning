'''
Binary Tree:
A Binary Tree is a tree data structure in which each node has at atmost 2 children, which are refereed to as:
*left child
*right child

               2 
             /   \
            7     5
          /   \    \
         2     6    9
              / \    
             5   11
Terminology:
*Root:Top Node is referred to as 'Root'. E.g. 2 above
*Left Child: 7 is left child of Node 2 
*Right Child: 5 is right child og Node 2
*Parent: 2 is parent of 7 & 5. Similary 7 is parent of 2 & 6
*GrandChild: 2(below 7) is grand child of 2(root)
*Leaves: Nodes at bottom of the tree are knows as Leaves. E.g. 5 & 11
*Node depth: The depth of a node is the number of edges from the root to the node.
*Node height: The height of a node is the number of edges from the node to the deepest leaf.
*Tree height: The height of a tree is a height of the root.
 Example: Node 2 is at level-1 or depth-1. 5,7 are at level-2 or depth-2. 2,6,9 are at level-3. 5,11 is at level-4. Thus tree has depth/height of 4.

Note:
This is somewhat similar to Linked-list, where Node(data,next) but in Binary Tree we can think this as of Node(value,leftNode & RightNode)


########Types of Binary tree#########
1.)Full Binary Tree/Strict Binary Tree(plane/proper tree)
A Binary Tree is full or strict if every node has exactly 0 or 2 children.

               18
           /       \  
         15         30  
        /  \        /  \
      100   4     40    50    

In Full Binary Tree,number of leaf nodes is equal to number of internal nodes plus one.

2.)Complete Binary Tree
Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible

          18
       /       \  
     15         30  
    /  \        /  \
  40    50     100  40
 /  \   /
8   7  9


###########Binary Tree Traversals#################
Process of visiting(checking/updating) each node in a tree data structure, exactly once.

Unlike Linked-Lists,one-dimension arrays, etc which are canonically traversed in linear order, trees may be traversed in multiple ways.
This may be 'depth-first' or 'breadth-first'

#Depth-First:
There are 3 common ways to traverse them in depth-first-order:
*In order
*Pre-order
*Post-order
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        ##root contains the root-value
        self.root = Node(root)

        ##when somebody calls BinaryTree(1), this will actually create:
        #self.root.value = 1
        #self.root.left = None
        #self.root.right = None

##Making Binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

'''
Following tree will be crated by above

                     1
                  /     \
                 2       3
               /   \    /  \
              4     5  6   7
'''

