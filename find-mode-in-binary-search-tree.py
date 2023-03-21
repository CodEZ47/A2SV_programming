# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ndict = defaultdict(int)
        ans = []
        def tree(node,ndict):
            if not node:
                return 100000
            
            nodel = tree(node.left,ndict)
            noder = tree(node.right,ndict)

            ndict[nodel] += 1
            ndict[noder] += 1

            return node.val
        
        tree(root,ndict)
        ndict[root.val] += 1

        ndict.pop(100000)

        arr = sorted(zip(ndict.keys(), ndict.values()))
        maxi = max(ndict.values())

        for tup in arr:
            if tup[1] == maxi:
                ans.append(tup[0])
        print(arr)
        return ans