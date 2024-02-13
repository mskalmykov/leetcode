from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while node != None and node.val != val:
            if val < node.val:
                node = node.left
            else:
                node = node.right

        return node

a = treeFromList([4,2,7,1,3])
print(Solution().searchBST(a, 2))
print(Solution().searchBST(a, 5))