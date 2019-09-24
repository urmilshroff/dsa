class Stack:
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.stack = []
        for i in range(size):
            self.stack.append(None)

    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, val):
        if self.top < self.size:
            self.stack[self.top] = val
            self.top += 1
            print(f'{val} pushed')

        else:
            print('Error: stack overflow')

    def pop(self):
        if self.top > 0:
            print(f'{self.stack[self.top-1]} popped')
            self.stack[self.top - 1] = None
            self.top -= 1

        else:
            print('Error: stack underflow')

    def peek(self):
        if self.is_empty():
            print('Stack empty')
        else:
            print(f'{self.stack[self.top-1]} peeked')


size = 5
stack = Stack(size)
stack.push(1)
stack.push(2)
stack.peek()
stack.push(3)
stack.pop()
stack.peek()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # overflow
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()  # underflow
