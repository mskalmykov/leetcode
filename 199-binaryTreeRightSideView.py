from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rView = []
        d1 = deque([root])
        d2 = deque()

        while d1:
            rView.append(d1[-1].val)
            while d1:
                node = d1.popleft()
                if node.left:
                    d2.append(node.left)
                if node.right:
                    d2.append(node.right)
            d1,d2 = d2,d1

        return rView
    
a = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(a))
b = TreeNode(1, None, TreeNode(3))
print(Solution().rightSideView(b))