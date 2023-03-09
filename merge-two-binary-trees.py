# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def tree(nodel,noder):
            if not nodel and not noder:
                return
            if not nodel:
                return noder
            if not noder:
                 return nodel
            
            nodel.val += noder.val

            a = tree(nodel.left, noder.left)
            b = tree(nodel.right, noder.right)

            nodel.left = a
            nodel.right = b

            return nodel
        
        return tree(root1,root2)