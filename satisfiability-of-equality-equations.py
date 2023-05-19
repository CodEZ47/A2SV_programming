class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equality = []
        non_equality = []
        size = defaultdict(int)
        rep = defaultdict(str)

        for eq in equations:
            if eq[1] == "=":
                equality.append(eq)
            else:
                non_equality.append(eq)
            
            if eq[0] not in rep:
                rep[eq[0]] = eq[0]
            if eq[-1] not in rep:
                rep[eq[-1]] = eq[-1]
            if eq[0] not in size:
                size[eq[0]] = 1
            if eq[-1] not in size:
                size[eq[-1]] = 1
        
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
            
            if size[node1] > size[node2]:
                rep[node2] = node1
                size[node1] += size[node2]
            else:
                rep[node1] = node2
                size[node2] += size[node1]
        
        for eq in equality:
            union(eq[0],eq[-1])

        for eq in non_equality:
            if find(rep[eq[0]]) == find(rep[eq[-1]]):
                return False
        
        return True