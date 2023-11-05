# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def bfs(root):
            if not root:
                return ""
            encoded = str(root.val)
            q = deque()
            q.append(root)

            while q:
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                    encoded +=  "|" + str(curr.left.val)
                else:
                    encoded += "|n"
                if curr.right:
                    q.append(curr.right)
                    encoded +=  "|" + str(curr.right.val)
                else:
                    encoded += "|n"
            
            return encoded

        ans = bfs(root)
        # print(ans)
        return ans

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        new_data = data.split("|")
        root = TreeNode(int(new_data[0]))
        new_data[0] = root
        n = len(new_data)
        prev = 1 #to be added to find left then +1 to find right
        # print(n)

        for idx, curr in enumerate(new_data):
            # print(root)
            if curr == "n":
                prev -= 1
                continue
            
            left_idx = idx + prev
            right_idx = idx + prev + 1

            if left_idx < n:
                if new_data[left_idx] == "n":
                    curr.left = None
                else:
                    curr.left = TreeNode(int(new_data[left_idx]))
                    new_data[left_idx] = curr.left
            if right_idx < n:
                if new_data[right_idx ] == "n":
                    curr.right = None
                else:
                    curr.right = TreeNode(int(new_data[right_idx ]))
                    new_data[right_idx ] = curr.right

            prev += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))