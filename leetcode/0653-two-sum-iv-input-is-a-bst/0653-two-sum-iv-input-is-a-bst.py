# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node1 = root
        if root.left:
            node2 = root.left
        elif root.right:
            node2 = root.right
        else:
            return False
        def dfs(root):
            if not root: return[]
            return dfs(root.left) + [root.val] + dfs(root.right)
        a = dfs(root)
        left = 0; right = len(a) - 1
        while left < right:
            s = a[left] + a[right]
            if s == k: return True
            if s < k: left += 1
            else: right -= 1
        return False
        