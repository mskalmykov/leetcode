from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        q.appendleft((root, 0))
        prevNode = root
        prevLevel = -1

        while q:
            n, level = q.pop()
            if level == prevLevel and n != None:
                n.next = prevNode
            if n:
                prevLevel = level
                prevNode = n
                q.appendleft((n.right, level + 1))
                q.appendleft((n.left, level + 1))

        return root


