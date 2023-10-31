# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        vis = set()
        to_delete = set(to_delete)
        q = deque()
        q.append((root,root,0))
        ans = []
        if not root:
            return ans
        if root.val not in to_delete:
            ans.append(root)


        while q:
            curr, par, pos = q.pop()

            if par.val in to_delete and curr.val not in to_delete:
                ans.append(curr)
            if curr.val in to_delete:
                if pos == 1:
                    par.left = None
                if pos == -1:
                    par.right = None
            
            if curr.left:
                q.append((curr.left, curr, 1))
            if curr.right:
                q.append((curr.right, curr, -1))
        

        return ans

            




