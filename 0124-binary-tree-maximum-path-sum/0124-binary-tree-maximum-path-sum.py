# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -10000000
        def dfs(node):
            nonlocal res
            if not node: return 0
            lmx = dfs(node.left)
            rmx = dfs(node.right)
            res = max(lmx+rmx+node.val, res)
            return max(0, max(lmx,rmx) + node.val)
        dfs(root)
        return res