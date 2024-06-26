from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        d = deque([self])
        l = []

        while d:
            node = d.popleft()
            if node:
                l.append(node.val)
                if node.left or node.right:
                    d.append(node.left)
                    d.append(node.right)
            else:
                l.append(None)
        return str(l)
    
def treeFromList(nodes: List) -> TreeNode:
    if not nodes:
        return None

    d1 = deque(nodes)

    root = TreeNode(d1.popleft())
    d2 = deque([root])

    while len(d1) > 1:
        n = d2.popleft()

        childVal = d1.popleft()
        if childVal != None:
            n.left = TreeNode(childVal)
            d2.append(n.left)

        childVal = d1.popleft()
        if childVal != None:
            n.right = TreeNode(childVal)
            d2.append(n.right)

    return root
