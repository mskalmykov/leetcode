from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sumsCount = 0

    def dfs(self, node: TreeNode, arr: List[int], targetSum: int, currentSum: int):
        if not node:
            return

        tmpSum = currentSum + node.val
        if tmpSum == targetSum:
            self.sumsCount += 1

        for v in arr:
            tmpSum -= v
            if tmpSum == targetSum:
                self.sumsCount += 1

        if (node.left == None) and (node.right == None):
            a = arr + [node.val]
        else:
            self.dfs(node.left, arr + [node.val], targetSum, currentSum + node.val)
            self.dfs(node.right, arr + [node.val], targetSum, currentSum + node.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
      
        self.dfs(root, [], targetSum, 0)
        
        return self.sumsCount
    

a = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))

print(Solution().pathSum(a, 8))

b = TreeNode(0, TreeNode(1), TreeNode(1))
print(Solution().pathSum(b, 1))

