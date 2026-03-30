# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        mx = int(1e9)

        if not root: return 0

        def dfs(x):
            if not x: return mx
            if not x.left and not x.right: return 1
            return min(dfs(x.left), dfs(x.right)) + 1
        return dfs(root)
        