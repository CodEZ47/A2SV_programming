class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        n = len(edges)
        size = [1] * (n+1)
        rep = defaultdict(int)

        for i in range(1,n+1):
            rep[i] = i
        
        
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
        

        for x,y in edges:
            # print(x,y)
            # print("in", rep)
            if find(rep[x]) == find(rep[y]):
                return [x,y]
            union(x,y)
            # print("out", rep)