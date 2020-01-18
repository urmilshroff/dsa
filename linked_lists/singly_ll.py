class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_beg(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at(self):
        pass

    def delete_beg(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            new_head = self.head.next
            self.head = None
            self.head = new_head

    def delete_end(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            current = self.head
            while current.next is not None:
                current = current.next
                if current.next is None:
                    current.val = None  # fix
                    break

    def delete_at(self):
        pass

    def search(self, elt):
        if self.head is None:
            print('Linked list is empty')

        else:
            current = self.head
            while current is not None:
                if current.val == elt:
                    print(f'{elt} found!')
                    break
                else:
                    current = current.next

    def reverse(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            pass

    def display(self):
        if self.head is None:
            print('Linked list is empty')

        else:
            print('Linked list is', end=' ')
            current = self.head
            while current is not None:
                print(current.val, end=' ')
                current = current.next
            print()


list = SinglyLL()

list.display()
list.insert_beg(1)
list.insert_end(2)
list.search(2)
list.insert_end(3)
list.insert_end(4)
list.delete_end()
list.search(4)

list.display()
