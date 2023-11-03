# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0

        def dfs(curr_node):
            nonlocal s
            if not curr_node:
                return
            
            if curr_node.val <= high and curr_node.val >= low:
                s += curr_node.val
            
            dfs(curr_node.left)
            dfs(curr_node.right)

        dfs(root)
        return s