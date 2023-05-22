# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0

        def dfs(curr, ancestors):
            nonlocal s
            if not curr:
                return 0
            
            # print( curr.val, ancestors)
            if ancestors[1] != 0 and ancestors[1] % 2 == 0:
                s += curr.val
            
            ancestors[1], ancestors[0] = ancestors[0], ancestors[1]
            ancestors[0] = curr.val

            val = ancestors.copy()
            dfs(curr.left,val)
            val = ancestors.copy()
            dfs(curr.right,val)
        
        dfs(root, [0,0])

        return s