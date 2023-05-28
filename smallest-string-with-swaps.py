class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        connect_dict = defaultdict(list)
        connect_idx = defaultdict(set)
        rep = defaultdict(str)
        size = defaultdict(int)



        for i in range(len(s)):
            rep[i] = i
            size[i] += 1
        


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
        
        for x,y in pairs:
            union(x,y)
        
        # print(rep)
        # print(find(rep[x]))
        
        for x,y in pairs:
            temp = find(rep[x])

            if x not in connect_idx[temp]:
                connect_dict[temp].append(s[x])
                connect_idx[temp].add(x)
            if y not in connect_idx[temp]:
                connect_dict[temp].append(s[y])
                connect_idx[temp].add(y)
        
        ans = list(s)
        vis = set()


        for key in connect_dict.keys():
            temp = connect_dict[key]
            idxs = list(connect_idx[key])
            temp.sort()
            idxs.sort()
            for i in range(len(temp)):
                ans[idxs[i]] = temp[i]
                vis.add(idxs[i])


        # print(connect_dict)
        # print(connect_idx)

        return "".join(ans)