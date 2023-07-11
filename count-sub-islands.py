class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        vis = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(coord):
            # print(coord)
            x = coord[0]
            y = coord[1]

            if x < 0 or x >= rows or y < 0 or y >= cols or grid2[x][y] == 0:
                return 1
            
            vis.add(coord)
            
            val = grid1[x][y]

            for neigh in directions:
                new_x = x + neigh[0]
                new_y = y + neigh[1]

                if (new_x, new_y) not in vis:
                    # print(new_x,new_y)
                    # KEEP TRACK OF WHERE YOU PLACE YOUR VALUES IN AND/OR THIS SHIT KEPT ME UP FOR TWO DAYS
                    val = dfs((new_x,new_y)) and val
            
            return val
        

        ans = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in vis and grid2[i][j] == 1:
                    if (dfs((i,j))):
                        ans += 1
        

        return ans