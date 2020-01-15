class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree is None:
        return 0

    elif depth(tree.left) >= depth(tree.right):
        return depth(tree.left) + 1

    elif depth(tree.left) < depth(tree.right):
        return depth(tree.right) + 1


tree = Node(10)
tree.left = Node(5)
tree.right = Node(20)
tree.right.left = Node(3)
tree.right.right = Node(7)
tree.right.left.left = Node(9)
tree.right.left.right = Node(18)

print(f'Depth of tree is {depth(tree)}')