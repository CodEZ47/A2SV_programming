class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        connected = [0] * n
        graph = defaultdict(list)


        if n == 1:
            return [0]




        for edge in edges:
            connected[edge[0]] += 1
            connected[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        queue = deque()

        for i in range(len(connected)):
            if connected[i] == 1:
                queue.append(i)
        
        temp = deque()
        # print(queue)
        while queue:
            l = len(queue)
            temp = queue.copy()
            for i in range(l):
                curr = queue.popleft()
                # print(queue)

                for neigh in graph[curr]:
                    connected[neigh] -= 1
                    if connected[neigh] == 1:
                        queue.append(neigh)
        

        return temp