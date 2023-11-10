class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def chk(row,col):
            return row > -1 and row < len(grid) and col > -1 and col < len(grid[0])

        visited = set()
        ctr = 0
        def traverse(g, row, col, v):
            nonlocal ctr
            if not chk(row, col) or not g[row][col]:
                    ctr += 1
                    return
                    
            visited.add((row,col))
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (new_row,new_col) not in v:
                    traverse(g,new_row,new_col,v)
        
        temp = ()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    temp = (i,j)
                    break
            if temp:
                break
        
        traverse(grid, temp[0], temp[1], visited)

        return ctr
