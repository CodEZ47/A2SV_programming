class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        incoming = [0] * numCourses
        queue = deque()
        pres = defaultdict(set)

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            incoming[edge[1]] += 1
        
        for i in range(len(incoming)):
            if not incoming[i]:
                queue.append(i)
        

        while queue:

            l = len(queue)

            for i in range(l):
                curr = queue.popleft()

                for child in graph[curr]:
                    pres[child].add(curr)
                    pres[child].update(pres[curr])
                    incoming[child] -= 1

                    if incoming[child] == 0:
                        queue.append(child)
        
        ans = []
        for query in queries:
            if query[0] in pres[query[1]]:
                ans.append(True)
            else:
                ans.append(False)

        return ans