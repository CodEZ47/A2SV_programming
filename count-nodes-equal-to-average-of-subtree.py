# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def tree(node):
            if not node:
                return [0,0,0]
            
            v1 = tree(node.left)
            v2 = tree(node.right)

            res = v1[2] + v2[2]
            print("res", res)

            if not node.left and not node.right:
                avg = node.val
            else:
                avg = (v1[0] + v2[0] + node.val)// (v1[1] + v2[1] + 1)
            print("avg", avg)
            print("node val", node.val)
            if avg == node.val:
                res =  res + 1
                print("in")
            
            print("-----------------------")
            
            return [(v1[0] + v2[0] + node.val), (v1[1] + v2[1] + 1), res]
        
        ans = tree(root)

        return ans[2]