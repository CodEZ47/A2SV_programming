class Solution:
    def shortestBridge(self, mat: List[List[int]]) -> int:
        queue = deque()

        def inRange(x,y):
            return x > -1 and x < len(mat) and y > -1 and y < len(mat[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def findFirst(queue):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] == 1:
                        queue.append((i,j))
                        return

        findFirst(queue)

        
        vis = set()
        k = 0 #currently flipped 0's
        # print(queue)
        

        # find the first island
        while queue:
            l = len(queue)
            # print(queue)

            for i in range(l):
                curr = queue.popleft()
                x = curr[0]
                y = curr[1]

                vis.add((x,y))

                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]

                    if inRange(new_x, new_y) and (new_x,new_y) not in vis and mat[new_x][new_y]:
                        queue.append((new_x,new_y))
                        vis.add((new_x,new_y))
            
        
        #add the first island to queue
        for coord in vis:
            queue.append(coord)

        #search for the second island
        def bfs(queue,k):
            while queue:
                l = len(queue)

                for i in range(l):
                    curr = queue.popleft()
                    x = curr[0]
                    y = curr[1]

                    for d in directions:
                        new_x = x + d[0]
                        new_y = y + d[1]

                        if inRange(new_x, new_y) and (new_x,new_y) not in vis:
                            if not mat[new_x][new_y]:
                                queue.append((new_x,new_y))
                                vis.add((new_x,new_y))
                            else:
                                return k
                
                k += 1

        ans = bfs(queue,k)

        return ans
        # return 6