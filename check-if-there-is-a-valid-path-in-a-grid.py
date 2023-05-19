class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        def inRange(coord):
            x = coord[0]
            y = coord[1]
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        
        first = [
            0, {1,4,6}, {2,3,4}, {1,4,6}, {1,3,5}, {2,3,4},{2,3,4}
        ]
        second = [
            0, {1,3,5}, {2,5,6}, {2,5,6}, {2,5,6}, {1,4,6}, {1,3,5}
        ]

        def direction(type, x,y):
            temp = []
            if type == 2:
                if inRange((x-1,y)) and grid[x-1][y] in first[grid[x][y]]:
                    temp.append([(x,y),(x-1,y)])
                if inRange((x+1,y)) and grid[x+1][y] in second[grid[x][y]]:
                    temp.append([(x,y),(x+1,y)])
            elif type == 1:
                if inRange((x,y-1)) and grid[x][y-1] in first[grid[x][y]]:
                    temp.append([(x,y),(x,y-1)])
                if inRange((x,y+1)) and grid[x][y+1] in second[grid[x][y]]:
                    temp.append([(x,y),(x,y+1)])
            elif type == 3:
                if inRange((x,y-1)) and grid[x][y-1] in first[grid[x][y]]:
                    temp.append([(x,y),(x,y-1)])
                if inRange((x+1,y)) and grid[x+1][y] in second[grid[x][y]]:
                    temp.append([(x,y),(x+1,y)])
            elif type == 4:
                if inRange((x,y+1)) and grid[x][y+1] in first[grid[x][y]]:
                    temp.append([(x,y),(x,y+1)])
                if inRange((x+1,y)) and grid[x+1][y] in second[grid[x][y]]:
                    temp.append([(x,y),(x+1,y)])
            elif type == 5:
                if inRange((x-1,y)) and grid[x-1][y] in first[grid[x][y]]:
                    temp.append([(x,y),(x-1,y)])
                if inRange((x,y-1)) and grid[x][y-1] in second[grid[x][y]]:
                    temp.append([(x,y),(x,y-1)])
            else:
                if inRange((x-1,y)) and grid[x-1][y] in first[grid[x][y]]:
                    temp.append([(x,y),(x-1,y)])
                if inRange((x,y+1)) and grid[x][y+1] in second[grid[x][y]]:
                    temp.append([(x,y),(x,y+1)])
            return temp
        

        edges = []
        n = len(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                    edges.extend(direction(grid[x][y],x,y))
        
        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        size = []
        rep = defaultdict(tuple)

        for i in range(n):
            for j in range(len(grid[0])):
                rep[(i,j)] = (i,j)
                size.append([1]*len(grid[0]))
        
        # print(size)
        
        
        def union(node1,node2):
            node1 = find(node1)
            node2 = find(node2)

            if node1 == node2:
                return
            
            if size[node1[0]][node1[1]] > size[node2[0]][node2[1]]:
                rep[node2] = node1
                size[node1[0]][node1[1]] += size[node2[0]][node2[1]]
            else:
                rep[node1] = node2
                size[node2[0]][node2[1]] += size[node1[0]][node1[1]]
        
        # print(edges)
        vis = set()

        for x,y in edges:
            # print(x,y)
            union(x,y)
        
        # print(rep)
        
        # print(find(rep[(0,0)]), find(rep[(n-1,len(grid[0])-1)]))
        
        return find(rep[(0,0)]) == find(rep[(n-1,len(grid[0])-1)])