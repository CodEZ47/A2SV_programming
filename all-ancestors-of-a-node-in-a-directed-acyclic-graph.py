class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        incoming = [0]*n
        ans = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            incoming[edge[1]] += 1

        queue = deque()

        for i in range(n):
            if not incoming[i]:
                queue.append(i)
            temp = set()
            ans.append(temp)

        while queue:
            parent = queue.popleft()
            temp = ans[parent].copy()
            temp.add(parent)
            for neigh in graph[parent]:
                ans[neigh] = set.union(ans[neigh],temp)
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    queue.append(neigh)
                
        

        for i in range(n):
            ans[i] = list(ans[i])
            ans[i].sort()
        return ans