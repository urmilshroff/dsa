class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, val):
        if len(self.queue) < self.size:
            self.queue.append(val)
            print(f'{val} enqueued')

        else:
            print('Error: queue full')

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

        else:
            print('Error: queue empty')

    def peek(self):
        if self.is_empty():
            print('Queue empty')
        else:
            print(f'{self.queue[0]} peeked')


size = 5
queue = Queue(size)
queue.enqueue(1)
queue.enqueue(2)
queue.peek()
queue.enqueue(3)
queue.dequeue()
queue.peek()
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
