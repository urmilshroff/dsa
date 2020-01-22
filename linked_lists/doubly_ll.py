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

    def length(self):
        if self.head is None or self.tail is None:
            return 0

        else:
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next

            return count

    def regular_search(self, elt):
        if self.head is None or self.tail is None:
            print('Linked list is empty')

        else:
            is_found = False
            count = 0
            current = self.head
            while current is not None:
                count += 1
                if current.val == elt:
                    is_found = True
                    break
                else:
                    current = current.next

            if is_found:
                print(f'{elt} found in {count} iterations using regular search')
            else:
                print(f'{elt} not found in the linked list')

    def runner_search(self, elt):
        if self.length() % 2 == 0:
            is_found = False
            count = 0
            current1 = self.head
            current2 = self.head

            while current2 is not None:
                count += 1
                if current2 is not None:
                    if current1.val == elt or current2.val == elt:
                        is_found = True
                        break
                    else:
                        current1 = current1.next
                        current2 = current1.next

                else:
                    break

            if is_found:
                print(f'{elt} found in {count} iterations using runner search')
            else:
                print(f'{elt} not found in the linked list')

        else:
            print('Length is odd, cannot apply runner technique!')

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
list.insert_beg(3)
list.insert_end(4)
list.insert_beg(2)
list.insert_end(5)
list.insert_beg(1)
list.insert_beg(0)
list.insert_end(6)
list.insert_end(7)
print(f'Length is {list.length()}')
list.display()
list.reverse()
list.delete_end()
list.regular_search(2)
list.runner_search(2)
list.delete_beg()
list.regular_search(6)
list.runner_search(6)