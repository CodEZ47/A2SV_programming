class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        
        for i in range(1, n-1):
            max_row = []
            for j in range(1, n-1):
                temp = [grid[i][j], grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i][j-1], grid[i][j+1], grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
                max_row.append(max(temp))
            ans.append(max_row)
        
        return ans