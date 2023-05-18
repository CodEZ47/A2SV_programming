class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        size = [1] * (n+1)
        rep = defaultdict(int)


        for i in range(1, n):
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
            
        

        for x,y,l in roads:
            union(x,y)
        
        # print(rep)
        
        mini = 100000
        for x,y,l in roads:
            if find(rep[1]) == find(rep[x]) and find(rep[1])== find(rep[y]):
                mini = min(l,mini)
        
        return mini