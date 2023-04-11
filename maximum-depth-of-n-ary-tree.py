"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ctr = 1
        
        def dfs(node,ctr):
            if not node.children:
                return ctr
            
            lst = []
            for child in node.children:
                lst.append(dfs(child,ctr+1))
            
            return max(lst)
            
        return dfs(root,ctr)
        
        
        
                
        