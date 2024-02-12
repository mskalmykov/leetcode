from typing import Optional
from bintree import TreeNode, treeFromList

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        parent = None
        isLeft = False
        found = False
        ans = None

        while node:
            if node.val == key:
                found = True
                break
            else:
                parent = node
            if node.val > key:
                node = node.left
                isLeft = True
            else:
                node = node.right
                isLeft = False
        
        if not found:
            return root
        
        if node.left == None and node.right == None:
            if not parent:
                return None
            if isLeft:
                parent.left = None
            else:
                parent.right = None
            return root
        
        if node.left:
            if isLeft:
                if parent:
                    parent.left = node.left
            else:
                if parent:
                    parent.right = node.left
            if node.right:
                n = node.left
                while n.right:
                    n = n.right
                n.right = node.right
            if parent:
                return root
            else:
                return node.left
        else:
            if isLeft:
                if parent:
                    parent.left = node.right
            else:
                if parent:
                    parent.right = node.right
            if parent:
                return root
            else:
                return node.right

    
a = treeFromList([5,3,6,2,4,None,7])
n = Solution().deleteNode(a, 3)
if n:
    print(n)
else:
    print('not found')
