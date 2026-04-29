# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return [0,0]
            lcoin,lst = dfs(node.left)
            rcoin,rst = dfs(node.right)
            coin = lcoin + rcoin + node.val
            st = lst + rst + 1
            res += abs(coin - st)
            return [coin,st]
        dfs(root)
        return res