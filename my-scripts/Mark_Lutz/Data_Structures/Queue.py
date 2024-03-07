class Queue:
    '''
    Queue:(FIFO - First In First Out)
    Let us talk about Queue as an abstract data type(ADT)
    Note: when we say ADT w.r.t. Data structures it means we are defining only the features/implmentations related to it and not implementation

    A Queue is exactly related to Queue in real world i.e. whatever goes in first, comes out first(FIFO structure).
    Do note that Stack(LIFO) is a structure in which both insertion/removal happens at same end(top-of-stack) E.g. Keeping/removing balls from bottle    But in Queue insertion must happens at one end(real/tail of queue) and removal must happen from other-end(front/head of queue)

    Thus Queue is a list or collection with restriction that inertion must happen at one end(rear/tail/end) and deletion must happen at other end(front/head/start)

    Operations with Queue:
    1. Enqueue(x) or Push(x): Insert element at end. Returns void/nothing
    2. Dequeue(x) or Pop(x): Delete element from starting and return deleted element
    3. Front() or Peek(): Returns Front/top/head/starting element
    4. is_empty(): Queue is empty or not
    5. is_full(): If size given to list/queue while creating then checking if it is full i.e. has reached that size

    Real-Scenario/Use-cases:
    Queue is most often used in a scenario where there is a shared resource but resource can handle/process/serve only 1 request at a time.
    In such scenario, it makes sense to make queue of requests i.e. request which goes first gets serves first.

    E.g. Let say we have a printer shared in a network. Any machine on network can send a print request to a printer and printer can only serve one request at a time or print only one document at at time. So, if a request comes to printer when its busy, printer can't say 'that am busy, come later', taht will be really rude of printer. So, what really happens is that the program that manages the printer puts the print request in the queue, so as long as there is something in the queue printer keeps picking the request from front of queue and serves it.

    Other example: processor
    '''

    def __init__(self):
        self.items = []

    def Enqueue(self,item):
        self.items.append(item)

    def Dequeue(self,item):
        return self.items.pop(0)

    def get_queue(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

if __name__ == '__main__':
    queue = Queue()
    queue.Enqueue(5)
    queue.Enqueue(4)
    queue.Enqueue(9)

    queue.get_queue()

    print(queue.Dequeue())
    queue.get_queue()
    
    print(queue.Dequeue())
    queue.get_queue()

    print(queue.is_empty())

    print(queue.Dequeue())
    queue.get_queue()
    
    print(queue.is_empty())
