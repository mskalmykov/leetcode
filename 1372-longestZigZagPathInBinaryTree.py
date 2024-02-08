from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, prevDir: int, pathLen: int):
            if node.left:
                if prevDir == 1:
                    dfs(node.left, -1, pathLen + 1)
                    self.maxLen = max(self.maxLen, pathLen + 1)
                else:
                    dfs(node.left, -1, 1)
            if node.right:
                if prevDir == -1:
                    dfs(node.right, 1, pathLen + 1)
                    self.maxLen = max(self.maxLen, pathLen + 1)
                else:
                    dfs(node.right, 1, 1)
                
        if root.left or root.right:
            self.maxLen = 1
            dfs(root, 0, 0)
            return self.maxLen
        else:
            return 0

a = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5, None, TreeNode(7, None, TreeNode(8))), TreeNode(6))))
b = TreeNode(1, TreeNode(2, None, TreeNode(4, TreeNode(5, None, TreeNode(7)), TreeNode(6))), TreeNode(3))
c = TreeNode(1)

print(Solution().longestZigZag(a))
print(Solution().longestZigZag(b))
print(Solution().longestZigZag(c))