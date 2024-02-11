from typing import Optional
from bintree import TreeNode, treeFromList
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        maxSumLevel = 0
        curLevel = 0
        d1 = deque([root])
        d2 = deque()

        while d1:
            levelSum = 0
            curLevel += 1
            while d1:
                node = d1.popleft()
                levelSum += node.val
                if node.left:
                    d2.append(node.left)
                if node.right:
                    d2.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                maxSumLevel = curLevel
            d1,d2 = d2,d1

        return maxSumLevel

a = treeFromList([1,7,0,7,-8])
print(Solution().maxLevelSum(a))
