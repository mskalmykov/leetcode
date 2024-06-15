from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        
        def helper(node: TreeNode) -> TreeNode:
            leftTail = helper(node.left) if node.left else None
            rightTail = helper(node.right) if node.right else None

            if leftTail:
                leftTail.right = node.right
                leftTail.left = None
                node.right = node.left
                node.left = None
            
            return rightTail or leftTail or node
        
        helper(root)

tree = treeFromList([1,2,5,3,4,None,6])
Solution().flatten(tree)
print(tree)

tree = treeFromList([])
Solution().flatten(tree)
print(tree)

tree = treeFromList([0])
Solution().flatten(tree)
print(tree)
