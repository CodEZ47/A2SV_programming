class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cost = []
        queue = deque()

        def inRange(x,y):
            return x > -1 and x < len(mat) and y > -1 and y < len(mat[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(mat)):
            cost.append([0]*len(mat[0]))
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
        
        vis = set()
        k = 0 #current cost
        # print(queue)
        while queue:
            l = len(queue)

            for i in range(l):
                curr = queue.popleft()
                x = curr[0]
                y = curr[1]

                cost[x][y] = k

                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]

                    if inRange(new_x, new_y) and (new_x,new_y) not in vis and mat[new_x][new_y]:
                        queue.append((new_x,new_y))
                        vis.add((new_x,new_y))
            
            k += 1


        return cost