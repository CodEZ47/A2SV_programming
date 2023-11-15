# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_dict = defaultdict(list)

        def traverse(curr,parent):
            if not curr:
                return
            
            if parent:
                node_dict[curr.val].append(parent.val)
            
            if curr.left:
                node_dict[curr.val].append(curr.left.val)
            if curr.right:
                node_dict[curr.val].append(curr.right.val)
            
            traverse(curr.left,curr)
            traverse(curr.right,curr)

        traverse(root,None)

        # print(node_dict)
        
        vis = set()
        ans = []
        def solve(curr,ctr):
            # print(curr,k)
            if curr in vis:
                return
            if ctr == k :
                ans.append(curr)
                return
            
            vis.add(curr)

            for neigh in node_dict[curr]:
                solve(neigh,ctr+1)
        
        solve(target.val,0)
        
        return ans




        