# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ctr = 0
        arr = []
        def tree(node,arr):
            nonlocal ctr
            if not node:
                return

            for i in range(len(arr)):
                arr[i] += node.val
                if arr[i] == targetSum:
                    ctr += 1
                
            if node.val == targetSum:
                ctr += 1
            
            arr.append(node.val)

            tree(node.left,arr.copy())
            tree(node.right,arr.copy())

        tree(root,arr)

        return ctr
