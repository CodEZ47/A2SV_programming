class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:


        m = 0
        n = 0
        rows = []
        cols = []
        size = defaultdict(int)
        rep = defaultdict(tuple)
        for x,y in stones:
            m = max(m,x)
            n = max(n,y)
            size[(x,y)] = 1
            rep[(x,y)] = (x,y)

        for x in range((m + 1)):
            rows.append([])
        for y in range(n + 1):
            cols.append([])



        for x,y in stones:
            rows[x].append((x,y))
            cols[y].append((x,y))
        
        
        def find(node):
            # print(node)
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        def union(node1,node2):
            node1 = find(node1)
            node2 = find(node2)

            if node1 == node2:
                return
            
            if size[node1] > size[node2]:
                rep[node2] = node1
                size[node1] += size[node2]
            else:
                rep[node1] = node2
                size[node2] += size[node1]
        
        
        def calc(arr):
            for k in range(len(arr)):
                n = len(arr[k])
                for i in range(n):
                    for j in range(n):
                        union(arr[k][i], arr[k][j])
        

        calc(rows)
        calc(cols)
        

        ctr = set()
        print(rep)

        for key in rep.keys():
            ctr.add(find(key))
        
        
        return len(stones) - len(ctr)