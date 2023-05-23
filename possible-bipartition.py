class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def dfs(node,color,parent,graph):
            if color[node]:
                if color[node] == color[parent]:
                    return False
                return True
            
            color[node] = color[parent] * -1
            val = True
            for child in graph[node]:
                if child != parent:
                    val = val and dfs(child,color,node,graph)
            
            return val


        graph = defaultdict(list)
        color = [0] * (n+1)
        color[0] = -1

        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        
        ans = True
        for i in range(1,n+1):
            if color[i] == 0:
                temp = dfs(i,color,0,graph)
            
            if temp == False:
                ans = False
        
        return ans