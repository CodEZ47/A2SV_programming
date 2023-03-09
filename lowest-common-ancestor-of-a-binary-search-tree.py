# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        def tree(node, p, q):            
            if p.val > node.val and q.val > node.val:
                return tree(node.right,p,q)
            elif p.val < node.val and q.val < node.val:
                return tree(node.left,p,q)
            else:
                return node
            
        return tree(root,p,q)