# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        lst = []
        lst.append(root)
        ctr = 0
        
        if lst == [None]:
            return ctr
        
        while lst:
            temp_lst = []
            for node in lst:
                temp_node = node
                if temp_node and temp_node.left != None:
                    temp_lst.append(temp_node.left)
                if temp_node and temp_node.right != None:
                    temp_lst.append(temp_node.right)
            
            ctr += 1
            lst = temp_lst
        
        return ctr