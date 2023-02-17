# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = []
        
        temp = [root]
        # print(temp)
        
        while temp:
            temp2 = []
            for node in temp:
                if node:
                    lst.append(node.val)
                    
                if node and node.left:
                    temp2.append(node.left)
                if node and node.right:
                    temp2.append(node.right)
                # print("temp2", temp2)
            
            temp = temp2
                
        # print(lst)
        lst.sort()
        min_ = 1000005
        for i in range(len(lst)-1):
            print(lst[i+1]-lst[i], min_)
            if lst[i+1] - lst[i] < min_:
                min_ = lst[i+1] - lst[i]
        
        
        # print(min_)
        return min_
            