class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mat = []
        comp = set()
        for i in range(n):
            mat.append([i,0])


        for i in range(len(roads)):
            mat[roads[i][0]][1] += 1
            mat[roads[i][1]][1] += 1
            comp.add((roads[i][0],roads[i][1]))
            comp.add((roads[i][1],roads[i][0]))
        
        maxi = 0
        for i in range(len(mat)):
            temp = 0
            for j in range(i+1, len(mat)):
                if (mat[i][0],mat[j][0]) in comp:
                    temp = mat[i][1] + mat[j][1] - 1
                else:
                    temp = mat[i][1] + mat[j][1]
                
                maxi = max(maxi,temp)
                
        return maxi