class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        queue = deque()
        incoming = [0] * len(quiet)
        ans = []

        for rel in richer:
            graph[rel[0]].append(rel[1])
            incoming[rel[1]] += 1
        
        # print(graph, incoming)

        for i in range(len(incoming)):
            ans.append(i)
            if not incoming[i]:
                queue.append(i)
        
        # print(queue)

        while queue:
            rng = len(queue)
            for i in range(rng):
                rich = queue.popleft()

                for poor in graph[rich]:
                    if quiet[ans[poor]] > quiet[ans[rich]]:
                        ans[poor] = ans[rich]

                    incoming[poor] -= 1
                    if incoming[poor] == 0:
                        queue.append(poor)
                    
        
        return ans