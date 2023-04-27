class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if grid[0][0] or grid[row-1][col-1]:
            return -1
        
        directions = [(0,1), (1,0), (-1,0), (0,-1),(-1,1), (1,-1), (-1,-1), (1,1)]

        def inRange(x,y):
            return x > -1 and x < len(grid) and y > -1 and y < len(grid[0])

        queue = deque()
        queue.append((0,0))
        visited = set((0,0))
        lvl = 1
        
        while queue:    
            temp = deque()

            while queue:
                pos = queue.popleft()
                if pos == (row-1,col-1):
                    return lvl
                visited.add(pos)
                for direction in directions:
                    new_row = pos[0] + direction[0]
                    new_col = pos[1] + direction[1]

                    if inRange((new_row),(new_col)) and not grid[new_row][new_col] and (new_row,new_col) not in visited:
                        temp.append(((new_row),(new_col)))
                        visited.add((new_row,new_col))
            
            queue = temp.copy()
            lvl += 1
        
        

        return -1




            


