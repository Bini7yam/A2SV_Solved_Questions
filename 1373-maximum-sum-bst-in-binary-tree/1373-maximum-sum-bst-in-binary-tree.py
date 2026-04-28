# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        snl = int(-1e8)
        def dfs(node):
            nonlocal res
            nmx = nmn = nsm = node.val
            dead = False
            if node.left:
                lsm, lmn, lmx = dfs(node.left)
                if lsm == snl or lmx >= node.val: dead = True
                nmn = lmn
                nsm += lsm
            if node.right:
                rsm, rmn, rmx = dfs(node.right)
                if rsm==snl or rmn <= node.val: dead = True
                nmx = rmx
                nsm += rsm
            if dead: return [snl,-1,-1]
            res = max(res, nsm)
            return [nsm, nmn, nmx]
        dfs(root)
        return res
        