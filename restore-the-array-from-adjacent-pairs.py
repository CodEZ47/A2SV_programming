class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        

        node = 0
        for key in graph.keys():
            if len(graph[key]) == 1:
                node = key
                break
        

        vis = set()
        ans = []
        def dfs(node):
            if node in vis:
                return
            
            vis.add(node)
            ans.append(node)

            for adj in graph[node]:
                dfs(adj)
        
        dfs(node)
        return ans