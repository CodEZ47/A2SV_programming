class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def inRange(x,y):
            return x > -1 and x < len(maze) and y > -1 and y < len(maze[0])

        ent = tuple(entrance)
        queue = deque()
        queue.append(ent)
        visited = set(ent)
        lvl = 0
        
        while queue:    
            temp = deque()

            while queue:
                pos = queue.popleft()
                visited.add(pos)
                for direction in directions:
                    new_row = pos[0] + direction[0]
                    new_col = pos[1] + direction[1]

                    if inRange((new_row),(new_col)) and maze[new_row][new_col] == "." and (new_row,new_col) not in visited:
                        temp.append(((new_row),(new_col)))
                        visited.add((new_row,new_col))
                    if not inRange((new_row),(new_col)) and pos != ent:
                        return lvl
            
            queue = temp.copy()
            lvl += 1
        
        

        return -1