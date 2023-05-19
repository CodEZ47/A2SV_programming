class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = defaultdict(str)
        edges = []

        for i in range(len(s1)):
            rep[s1[i]] = s1[i]
            rep[s2[i]] = s2[i]
            edges.append([s1[i],s2[i]])
        

        # print(edges)
        

        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        def union(node1,node2):
            node1 = find(node1)
            node2 = find(node2)

            if node1 == node2:
                return
            
            if node1 <= node2:
                rep[node2] = node1
            else:
                rep[node1] = node2
        

        for x,y in edges:
            union(x,y)
        
        # print(rep)
        ans = ""
        for char in baseStr:
            # print(char)
            if char in rep:
                ans += find(char)
            else:
                ans += char
            # print(ans)


        return ans