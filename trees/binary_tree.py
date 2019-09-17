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


def inorder(tree):  # left -> middle -> right
    if tree is None:
        return None

    if tree.left is not None:
        inorder(tree.left)

    print(tree.val, end=' ')  # middle

    if tree.right is not None:
        inorder(tree.right)


def preorder(tree):  # middle -> left -> right
    if tree is None:
        return None

    print(tree.val, end=' ')  # middle

    if tree.left is not None:
        preorder(tree.left)

    if tree.right is not None:
        preorder(tree.right)


def postorder(tree):  # left -> right -> middle
    if tree is None:
        return None

    if tree.left is not None:
        postorder(tree.left)

    if tree.right is not None:
        postorder(tree.right)

    print(tree.val, end=' ')  # middle


tree = Node(4)
tree.left = Node(2)
tree.right = Node(6)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.left = Node(5)
tree.right.right = Node(7)

print(f'Depth of the tree is {depth(tree)}')
print('Inorder traversal is')
inorder(tree)
print('\nPreorder traversal is')
preorder(tree)
print('\nPostorder traversal is')
postorder(tree)
