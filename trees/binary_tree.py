class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(node):
    if node is not None:
        print(node.val)
        traverse(node.left)
        traverse(node.right)


def count(node):
    if node is None:
        return 0
    else:
        return count(node.left) + count(node.right) + 1


def depth(node):
    if node is None:
        return 0

    elif depth(node.left) >= depth(node.right):
        return depth(node.left) + 1

    elif depth(node.left) < depth(node.right):
        return depth(node.right) + 1


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(3)
root.right.right = Node(7)
root.right.left.left = Node(9)
root.right.left.right = Node(18)

print(f'Depth of tree is {depth(root)}')
print(f'Number of nodes is {count(root)}')
print('Tree traversed is')
traverse(root)
