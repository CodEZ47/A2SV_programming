class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
                graph[y].append(x)
                graph[x].append(y)
        
        vis = set()
        def dfs(node):
            if node in vis:
                return 0
            vis.add(node)
            total = 0
            for child in graph[node]:
                total += dfs(child)

            if hasApple[node] or total > 0:
                total += 2
            
            return total
        
        ans = dfs(0)

        if not ans:
            return ans
        return ans - 2