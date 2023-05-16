from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        graph = defaultdict(list)
        vis = set()

        for i in range(V):
            graph[i] = adj[i]

        def dfs(node, parent):
            # print(vis, node)
            if node in vis:
                return False
            
            vis.add(node)
            
            val = True
            for neigh in graph[node]:
                if neigh != parent:
                    val = val and dfs(neigh,node)
            
            return val

        ans = True
        for key in graph.keys():
            if key not in vis:
                ans = ans and dfs(key, -1)

        return not ans