from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def __init__(self) -> None:
        self.totalSum = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node: TreeNode, numStr: str) -> None:
            t = numStr + str(node.val)
            if not node.left and not node.right:
                self.totalSum += int(t)
            if node.left:
                helper(node.left, t)
            if node.right:
                helper(node.right, t)

        helper(root, '')

        return self.totalSum

print(Solution().sumNumbers(treeFromList([1,2,3])))
print(Solution().sumNumbers(treeFromList([4,9,0,5,1])))
