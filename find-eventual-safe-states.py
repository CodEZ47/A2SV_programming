class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]):
        
        g_dic = defaultdict(list)
        color = [0]*(len(graph))

        for i in range(len(graph)):
            g_dic[i] = graph[i]
        
        ans = set()

        def dfs(node):
            nonlocal ans
            if not g_dic[node] or color[node] == 2:
                ans.add(node)
                return True
            if color[node] == 1:
                return False
            color[node] = 1

            val = True
            for neigh in g_dic[node]:
                 comp = dfs(neigh)
                 val = val and comp
            if val:
                color[node] = 2
                ans.add(node)

            return val

        
        
        for node in g_dic.keys():
            if color[node] == 0:
                dfs(node)
        ans = list(ans)
        ans.sort()
        return ans