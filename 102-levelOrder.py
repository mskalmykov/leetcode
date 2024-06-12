from typing import Optional, List
from bintree import TreeNode, treeFromList
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                n = queue.popleft()
                level.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            result.append(level)

        return result

print(Solution().levelOrder(treeFromList([3,9,20,None,None,15,7])))
print(Solution().levelOrder(treeFromList([1])))
print(Solution().levelOrder(treeFromList([])))