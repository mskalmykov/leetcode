class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.firstNode = None
        self.ans = None
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def checkNode(node: TreeNode) -> bool:
            if not node:
                return False
            if node == p or node == q:
                if self.firstNode:
                    return True
                else:
                    self.firstNode = node
                    if checkNode(node.left) or checkNode(node.right):
                        self.ans = self.firstNode
                    return True
                
            foundLeft = checkNode(node.left)
            foundRight = checkNode(node.right)
            if foundLeft and foundRight:
                self.ans = node
                return True
            return foundLeft or foundRight
            
        checkNode(root)
        return self.ans
