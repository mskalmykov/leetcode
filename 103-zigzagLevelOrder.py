from typing import Optional, List
from bintree import TreeNode, treeFromList
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        lst = []
        queue = deque([root])
        isLeft = True

        while queue:
            level = []
            for _ in range(len(queue)):
                if isLeft:
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    level.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            lst.append(level)
            isLeft = not isLeft

        return lst

print(Solution().zigzagLevelOrder(treeFromList([3,9,20,None,None,15,7])))
print(Solution().zigzagLevelOrder(treeFromList([1])))
print(Solution().zigzagLevelOrder(treeFromList([])))
