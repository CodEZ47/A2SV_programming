# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def build(node,comp):
            if comp < node.val:
                if node.left:
                    build(node.left,comp)
                else:
                    node.left = TreeNode(comp)
            else:
                if node.right:
                    build(node.right,comp)
                else:
                    node.right = TreeNode(comp)
        
        for i in range(1,len(preorder)):
            build(root,preorder[i])
        

        return root