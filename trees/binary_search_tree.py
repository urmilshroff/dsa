class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(tree):  # l-m-r
    if tree is None:
        return None

    if tree.left is not None:
        inorder(tree.left)

    print(tree.val, end=' ')

    if tree.right is not None:
        inorder(tree.right)


def preorder(tree):  # m-l-r
    if tree is None:
        return None

    print(tree.val, end=' ')

    if tree.left is not None:
        inorder(tree.left)

    if tree.right is not None:
        inorder(tree.right)


def postorder(tree):  # l-r-m
    if tree is None:
        return None

    if tree.left is not None:
        inorder(tree.left)

    if tree.right is not None:
        inorder(tree.right)

    print(tree.val, end=' ')


def is_bst(root):
    if root is None:
        return True

    elif is_left_lesser(root) and is_right_greater(root):
        return True

    else:
        return False


def is_left_lesser(root):
    if root.left is None:
        return True

    elif root.left.val <= root.val and is_bst(root.left):
        return True

    else:
        return False


def is_right_greater(root):
    if root.right is None:
        return True

    elif root.right.val > root.val and is_bst(root.right):
        return True

    else:
        return False


tree = Node(10)  # root node
tree.left = Node(5)
tree.right = Node(15)
tree.left.left = Node(1)
tree.left.right = Node(7)
tree.right.left = Node(12)
tree.right.right = Node(17)

inorder(tree)  # l-m-r
print()
preorder(tree)  # m-l-r
print()
postorder(tree)  # l-r-m
print()
print(f'Is binary search tree: {is_bst(tree)}')
