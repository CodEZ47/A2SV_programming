class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [0]*numCourses

        graph = defaultdict(list)
        
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])
            incoming[preq[1]] += 1

        queue = deque()

        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
        
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for neigh in graph[curr]:
                incoming[neigh] -= 1

                if incoming[neigh] == 0:
                    queue.append(neigh)
        
        if len(ans) != len(incoming):
            return False

        return True

            