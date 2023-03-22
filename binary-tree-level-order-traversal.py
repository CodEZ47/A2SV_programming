# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def tree(node,h=0):
            if node:
                ans[h].append(node.val)
                tree(node.left, h+1)
                tree(node.right, h+1)
        tree(root)
        
        return ans.values()