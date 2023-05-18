class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        size = [1] * n
        rep = defaultdict(int)

        for i in range(n):
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
            union(x,y)
        
        
        return find(source) == find(destination)