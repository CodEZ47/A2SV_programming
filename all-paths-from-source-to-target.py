class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path_dict = defaultdict(set)
        i = 0
        for path in graph:
            for p in path:
                path_dict[i].add(p)
            i += 1
        
        print(path_dict)
        
        res = []
        lst = [0]
        def dfs(curr_path):
            if curr_path == len(graph)-1:
                res.append(lst.copy())
                return

            for neigh in path_dict[curr_path]:
               lst.append(neigh)
               dfs(neigh)
               lst.pop()
            
            return res

        ans = dfs(0)

        return ans