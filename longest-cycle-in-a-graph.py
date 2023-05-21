class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        graph = defaultdict(list)
        no_nodes = len(edges) - 1
        incoming = [0] * (len(edges))

        for i in range(no_nodes+1):
            if edges[i] != -1:
                graph[i].append(edges[i])
                incoming[edges[i]] += 1
        
        vis = set()
        cycles = -1
        def dfs(node):
            nonlocal cycles
            if node in vis:
                return [node, 1]
            
            val = [-1,-1]
            vis.add(node)

            for child in graph[node]:
                temp = dfs(child)
                if val[1] < temp[1]:
                    val = temp
            
            if val[0] == node:
                cycles = max(cycles,val[1])
            else:
                val[1] += 1

            return val
        
        for i in range(no_nodes+1):
            if i not in vis:
                dfs(i)


        return cycles