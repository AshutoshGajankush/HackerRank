def getHeight(self, root):
    if root is None:
        return 0
    q = []
    q.append(root) #Start from the root
    height = 0

    while(True):
        nodeCount = len(q) # Will check if the traversing has reached its end.
        if nodeCount == 0 : # Will print the length of the tree when end of the tree is reached
            return height-1 
 
        height += 1 # adding height 
        while(nodeCount > 0): #While list q is not empty
            node = q[0] # point to the first element
            q.pop(0) # remove the node used
            if node.left is not None: # if that node contains left child
                q.append(node.left) # Append it to the list
            if node.right is not None: # if the node contains right child
                q.append(node.right) # Append it to the list
            nodeCount -= 1 # Decrease the list count by one every time.
        