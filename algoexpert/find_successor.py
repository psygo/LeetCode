class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    ordered = []

    def traverseHelper(tree, ordered):
        if tree is None:
            return
        else:
            traverseHelper(tree.left, ordered)
            ordered.append(tree.value)
            traverseHelper(tree.right, ordered)

    traverseHelper(tree, ordered)

    vIndex = ordered.index(node.value)
    if vIndex == -1 or vIndex == len(ordered) - 1:
        return None
    else:
        return ordered[vIndex + 1]


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.parent = root
root.right = BinaryTree(3)
root.right.parent = root
root.left.left = BinaryTree(4)
root.left.left.parent = root.left
root.left.right = BinaryTree(5)
root.left.right.parent = root.left
root.left.left.left = BinaryTree(6)
root.left.left.left.parent = root.left.left
node = root.left.right

print(findSuccessor(root, node))
