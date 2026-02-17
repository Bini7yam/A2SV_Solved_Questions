# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(x):#return max_including, max_not_including
            if not x: return [0,0]
            mxi = mxni = 0
            v1,v2 = dfs(x.left)
            mxi = v2
            mxni = max(v1,v2)
            v1,v2 = dfs(x.right)
            mxi += v2 + x.val
            mxni += max(v1,v2)
            print(x.val, mxi, mxni)
            return [mxi,mxni]
        return max(dfs(root))

        