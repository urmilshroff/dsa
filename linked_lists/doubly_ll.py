class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display_list(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next

    def insert_head(self, val):
        if self.head is None:
            self.head = Node(val)
            self.head.next = self.tail

        else:
            current = Node(val)
            self.head.previous = current
            current.next = self.head
            self.head = current

    def insert_tail(self, val):
        if self.head is None:
            self.insert_head(val)

        elif self.tail is None:
            self.tail = Node(val)

        else:
            current = Node(val)
            self.tail.next = current
            current.previous = self.tail

    def delete_head(self):
        if self.head is None:
            print('No head to delete')

        else:
            current = self.head
            self.head = self.head.next
            current = None

    def delete_tail(self):
        if self.tail is None:
            print('No tail to delete')

        else:
            current = self.tail
            self.tail = self.tail.previous
            current = None


list = DoublyLL()

list.display_list()  # empty
list.insert_head(1)
list.insert_tail(2)
# list.display_list()  # 1 2
list.insert_tail(3)
list.delete_head()
# list.display_list()  # 2 3
list.insert_tail(4)
# list.search(4)  # 4 found in position 4
list.display_list()  # 4 2 3
list.delete_tail()
# list.search(4)  # not found
list.delete_tail()
list.delete_tail()
list.display_list()  # empty
