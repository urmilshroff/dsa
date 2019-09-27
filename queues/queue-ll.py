class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self, size):
        self.size = size
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False

    def enqueue(self, val):
        item = Node(val)

        if self.is_empty():
            self.front = item

        self.rear = item
        self.rear.next = item
        print(f'{self.rear.val} enqueued!')

    def dequeue(self):
        if self.is_empty():
            print('Error: queue empty')
        else:
            self.front = self.front.next
            print(f'{self.front.val} dequeued!')
            if self.front is None:
                self.rear = None


size = 5
queue = Queue(size)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)  # overflow
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # underflow
