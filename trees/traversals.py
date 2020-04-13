class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInOrder(root):
    if root:
        printInOrder(root.left)

        print(root.val),

        printInOrder(root.right)


def printPreOrder(root):
    if root:

        print(root.val),

        printPreOrder(root.left)

        printPreOrder(root.right)


def printPostOrder(root):
    if root:
        printInOrder(root.left)

        printInOrder(root.right)

        print(root.val),


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("PreOrder traversal of binary tree is")
printPreOrder(root)

print("\nInorder traversal of binary tree is")
printInOrder(root)

print("\nPostorder traversal of binary tree is")
printPostOrder(root)
