class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def chk(row,col):
            return row > -1 and row < len(grid) and col > -1 and col < len(grid[0])

        visited = set()
        ctr = 0
        def traverse(g, row, col, v):
            nonlocal ctr
            if not chk(row, col) or not g[row][col]:
                    return
            ctr += 1
            visited.add((row,col))
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (new_row,new_col) not in v:
                    traverse(g,new_row,new_col,v)
        
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    ctr = 0
                    traverse(grid,i,j,visited)
                    maxi = max(maxi,ctr)
                    
        
        return maxi