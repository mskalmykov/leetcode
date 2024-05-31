from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            t = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = t
            return root

print(Solution().invertTree(treeFromList([4,2,7,1,3,6,9])))
print(Solution().invertTree(treeFromList([2,1,3])))
print(Solution().invertTree(treeFromList([])))