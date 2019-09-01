class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next

    def search(self, find):
        if self.head is None:
            print('Linked list is empty')

        else:
            current = self.head
            pos = 0

            while current is not None:
                if current.val == find:
                    print(f'{find} found in position {pos}')
                    break

                pos += 1
                current = current.next

    def insert_head(self, val):
        if self.head is None:
            self.head = Node(val)

        else:
            current = Node(val)
            current.next = self.head
            self.head = current

    def insert_tail(self, val):
        if self.head is None:
            self.head = Node(val)

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def delete_head(self):
        if self.head is None:
            print('No head to delete')

        else:
            current = self.head
            self.head = self.head.next
            current = None

    def delete_tail(self):
        if self.head is None:
            print('No tail to delete')

        else:
            current = self.head
            while current.next is not None:
                current = current.next  # reach the end of the list
            current = None


list = SinglyLL()

list.display_list()  # empty
list.insert_head(1)
list.insert_tail(2)
list.display_list()  # 1 2
list.insert_tail(3)
list.delete_head()
list.display_list()  # 2 3
list.insert_tail(4)
list.search(4) # 4 found in position 4
list.display_list()  # 4 2 3
list.delete_tail()
list.search(4)  # not found
list.delete_tail()
list.delete_tail()
list.display_list()  # empty
