# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = [root]
        if not root:
            return root
        
        while temp:
            node = temp.pop()
            if node:
                node.left, node.right = node.right, node.left
                temp += node.left, node.right
        
        return root