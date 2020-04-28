class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  # head
        self.rear = None  # tail

    def enqueue(self, val):
        node = Node(val)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            node.next = self.rear
            self.rear = node

    def dequeue(self):
        if self.front is not None:
            current = self.rear

            while current.next is not self.front:
                current = current.next

            current.next = None
            self.front = current

        return self.front.val

    def display(self):
        if self.rear is None or self.front is None:
            print('Queue is empty')

        else:
            print('[REAR]', end=' ')
            current = self.rear

            while current is not None:
                print(current.val, end=' -> ')
                current = current.next

            print('None [FRONT]')


queue = Queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.display()
