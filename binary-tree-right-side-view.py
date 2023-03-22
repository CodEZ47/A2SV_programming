# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(list)

        def tree(node,h=0,s = 1):
            if node:
                ans[h].append(node.val)
                tree(node.right, h+1, s = 1)
                tree(node.left, h+1, s = 0)
        tree(root)
        output = []
        for val in ans.values():
            if val:
                output.append(val[0])
        
                
        return output