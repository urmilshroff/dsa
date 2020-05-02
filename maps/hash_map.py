class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, key, val):
        new_node = Node(key, val)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get_data(self, key):
        if self.head is not None:
            current = self.head

            while current is not None:
                if current.key == key:
                    return 'Value for ' + key + ' is ' + str(current.val)
                else:
                    current = current.next  # isn't this O(n)?

        return 'Key does not exist in map'


array = [LinkedList() for i in range(5)]  # creates 5 linked lists

while True:
    key = input('Enter key to add: ')
    val = input('Enter respective value: ')

    key_hash = hash(key)
    index = key_hash % len(array)
    array[index].add_data(key, val)  # adds data in respective linked list

    cont = input('Continue? y/n: ')
    if cont == 'n':
        break

while True:
    key = input('Enter key to get value: ')
    key_hash = hash(key)
    index = key_hash % len(array)
    print(array[index].get_data(key))  # gets data from respective linked list

    cont = input('Continue? y/n: ')
    if cont == 'n':
        break
