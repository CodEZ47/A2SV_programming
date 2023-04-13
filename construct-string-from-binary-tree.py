# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        
        def dfs(node):
            nonlocal res
            if not node:
                return ""
            res = str(node.val)
            if node.left:
                res += "(" + str(dfs(node.left)) + ")"
            
            if not node.left and node.right:
                res += "()"
            
            if node.right:
                res += "(" + str(dfs(node.right)) + ")"
            
            return res
        
        ans = dfs(root)
        
        return ans
        