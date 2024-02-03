class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countGood(r, max) -> int:
            if not r:
                return 0
            if r.val >= max:
                return 1 + countGood(r.left, r.val) + countGood(r.right, r.val)
            else:
                return countGood(r.left, max) + countGood(r.right, max)
                
        return countGood(root, -10001)
    

a = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
b = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
c = TreeNode(1)

print(Solution().goodNodes(a))
print(Solution().goodNodes(b))
print(Solution().goodNodes(c))

