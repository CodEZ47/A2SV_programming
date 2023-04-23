class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_dict = defaultdict(set)
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] and row != col:
                    city_dict[row+1].add(col+1)
        
        vis = set()
        ctr = 0
        print(city_dict)
        
        def dfs(city):
            nonlocal ctr
            nonlocal vis
            if city in vis:
                return
            vis.add(city)
            for c in city_dict[city]:
                dfs(c)
        
        for i in range(1, len(isConnected)+1):
            if i in city_dict and i not in vis:
                dfs(i)
                ctr += 1
            elif i in vis:
                continue
            else:
                ctr += 1
        
        return ctr
            
            