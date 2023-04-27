# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        avgs = []
        lvl = 0

        queue.append(root)

        while queue:
            avgs.append(0)
            div = 0
            temp = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                avgs[lvl] += node.val
                div += 1
            queue.extend(temp)
            avgs[lvl] = avgs[lvl] / div
            lvl += 1

            




        return avgs
        # for i in range(len(s))

