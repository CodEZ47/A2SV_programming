class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vals = defaultdict(list)
        nums = set()


        for i, eq in enumerate(equations):
            x,y = eq
            vals[x].append([y,values[i]])
            vals[y].append([x,1/values[i]])


        
        def bfs(s,e):
            if s not in vals or e not in vals:
                return -1
            
            q = deque()
            vis = set()
            q.append([s,1])
            vis.add(s)

            while q:
                curr, w_prod = q.popleft()

                if curr == e:
                    return w_prod
                
                for neigh, weight in vals[curr]:
                    if neigh not in vis:
                        q.append([neigh, w_prod * weight])
                        vis.add(neigh)
                
            
            return - 1
        

        ans = []

        for q in queries:
            s,e = q

            ans.append(bfs(s,e))
        
        return ans

            


            