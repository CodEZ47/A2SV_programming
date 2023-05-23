class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)

        def calc(x,y):
            x1 = x[0]
            x2 = y[0]
            y1 = x[1]
            y2 = y[1]

            return (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                distance = calc(bombs[i], bombs[j])
                # print(distance, bombs[i][2], bombs[j][2])

                if bombs[i][2] >= distance:
                    graph[i].append(j)
                if bombs[j][2] >= distance:
                    graph[j].append(i)
        

        print(graph)

        
        def dfs(node):
            if node in vis:
                return 0
                
            vis.add(node)
            temp = 1
            for child in graph[node]:
                if child not in vis:
                    temp += dfs(child)
            
            return temp
            
        maxi = 1
        for i in range(len(bombs)):
            vis = set()
            curr = dfs(i)
            maxi = max(maxi, curr)
            print(i,curr)


        return maxi