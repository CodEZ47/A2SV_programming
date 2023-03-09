# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def tree(nodel,noder):
            if not nodel and not noder:
                return True
            if not nodel or not noder:
                return False
            val = nodel.val == noder.val

            if not val:
                return False

            a = tree(nodel.left, noder.left)
            b = tree(nodel.right, noder.right)

            return a and b
        
        return tree(p,q)