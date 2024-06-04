from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root.val == targetSum \
            and root.left == None \
            and root.right == None:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)

print(Solution().hasPathSum(treeFromList([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))
print(Solution().hasPathSum(treeFromList([1,2,3]), 5))
print(Solution().hasPathSum(treeFromList([]), 0))