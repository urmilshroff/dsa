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
            new_node.prev = new_node.prev
            self.tail = new_node

    def insert_at(self):
        pass

    def delete_beg(self):
        pass

    def delete_end(self):
        pass

    def delete_at(self):
        pass

    def search(self):
        pass

    def reverse(self):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            current = self.tail
            while current is not None:
                print(current.val, end='')
                current = current.prev

    def display(self):
        pass


list = DoublyLL()
