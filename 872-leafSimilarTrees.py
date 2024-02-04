from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaves(node: TreeNode) -> List[int]:
            if not node:
                return []
            elif (node.left == None) and (node.right == None):
                return [node.val]
            else:
                return findLeaves(node.left) + findLeaves(node.right)
        
        return findLeaves(root1) == findLeaves(root2)

    
a = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
b = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

print(Solution().leafSimilar(a, b))
