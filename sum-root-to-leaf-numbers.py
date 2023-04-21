# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = "0"

        def dfs(node,v):
            if not node.right and not node.left:
                v += str(node.val)
                return int(v)
            
            v += str(node.val)
            # print(v)

            l = 0
            r = 0
            if node.left:
                l = dfs(node.left,v)
            if node.right:
                r = dfs(node.right,v)

            return l + r
        
        return dfs(root,val)