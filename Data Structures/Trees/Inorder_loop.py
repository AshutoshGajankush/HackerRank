"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def inOrder(root):
    stack = []
    while root or stack:
        while root!=None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print root.data,
        root = root.right
            