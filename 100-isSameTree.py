from typing import Optional
from bintree import TreeNode, treeFromList
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:  # both None
            return True
        
        pD = deque()
        qD = deque()

        pD.append(p)
        qD.append(q)

        while pD and qD:
            pNode = pD.pop()
            qNode = qD.pop()

            if pNode == qNode:   # both None
                continue
            elif pNode and qNode and pNode.val == qNode.val:
                pD.appendleft(pNode.left)
                pD.appendleft(pNode.right)
                qD.appendleft(qNode.left)
                qD.appendleft(qNode.right)
            else:
                return False
        if pD or qD:
            return False
        else:
            return True

print(Solution().isSameTree(treeFromList([1,2,3]), treeFromList([1,2,3])))
print(Solution().isSameTree(treeFromList([1,2]), treeFromList([1,None,2])))
print(Solution().isSameTree(treeFromList([1,2,1]), treeFromList([1,1,2])))