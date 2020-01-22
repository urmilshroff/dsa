class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self, val):
        new_node = Node(val)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at(self):
        pass

    def delete_beg(self):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            current = self.head.next
            self.head = None
            current.prev = None
            self.head = current

    def delete_end(self):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            current = self.tail.prev
            self.tail = None
            current.next = None
            self.tail = current

    def delete_at(self):
        pass

    def search(self):
        pass

    def reverse(self):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            print('Reversed linked list is', end=' ')
            current = self.tail
            while current is not None:
                print(current.val, end=' ')
                current = current.prev
            print()

    def display(self):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            print('Linked list is', end=' ')
            current = self.head
            while current is not None:
                print(current.val, end=' ')
                current = current.next
            print()


list = DoublyLL()

list.display()
list.insert_beg(1)
list.insert_end(2)
list.insert_beg(0)
list.insert_end(3)
list.display()
list.delete_beg()
list.delete_end()
list.display()
list.reverse()