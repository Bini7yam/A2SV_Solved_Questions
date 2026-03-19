# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def gmx(node): return gmx(node.right) if node.right else node.val
        def dmx(node):
            if node.right:
                node.right = dmx(node.right)
                return node
            return node.left
        def gmn(node): return gmn(node.left) if node.left else node.val
        def dmn(node):
            if node.left:
                node.left = dmn(node.left)
                return node
            return node.right
            
        def dfs(node):
            if not node: return None
            if node.val == key:
                if node.left:
                    node.val = gmx(node.left)
                    node.left = dmx(node.left)
                    return node
                elif node.right:
                    node.val = gmn(node.right)
                    node.right = dmn(node.right)
                    return node
                else: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        return dfs(root)
        
                
                
        