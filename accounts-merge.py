class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep = defaultdict(str)
        size = defaultdict(int)
        name = defaultdict(str)

        for account in accounts:
            n = account[0]

            for i in range(1,len(account)):
                rep[account[i]] = account[i]
                size[account[i]] += 1
                name[account[i]] = n #not really need could be optimized later
        
        # print(rep)
        # print(size)
        # print(name)


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
        
        emails = defaultdict(set)
        for account in accounts:
            for i in range(2,len(account)):
                union(account[1], account[i])
        
        for key in rep.keys():
            emails[find(rep[key])].add(key)

        # print(emails)
        
        ans = []

        for key in emails.keys():
            temp = []
            temp.append(name[key])
            e = list(emails[key])
            e.sort()
            # print(temp,e,key)
            temp.extend(e)
            ans.append(temp)
        
        # print(ans)
        return ans