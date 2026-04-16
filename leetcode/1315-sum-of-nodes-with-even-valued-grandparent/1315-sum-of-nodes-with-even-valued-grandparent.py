# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, ep, egp):
            if not node: return
            nonlocal res
            if egp: res += node.val
            e = node.val % 2 == 0
            dfs(node.left, e, ep)
            dfs(node.right, e, ep)
        dfs(root,0,0)
        return res