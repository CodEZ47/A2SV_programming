class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        sums = set()
        set_ = set()
        ctr = 0
        
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                sums = set()
                sums.add(grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]) 
                sums.add(grid[i][j-1] + grid[i][j] + grid[i][j+1]) 
                sums.add(grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])
                
                sums.add(grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]) 
                sums.add(grid[i-1][j] + grid[i][j] + grid[i+1][j]) 
                sums.add(grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1])
                
                sums.add(grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]) 
                sums.add(grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1])
                
                set_ = set()
                set_.add(grid[i][j])
                set_.add(grid[i+1][j+1])
                set_.add(grid[i-1][j-1])
                set_.add(grid[i-1][j])
                set_.add(grid[i][j-1])
                set_.add(grid[i+1][j])
                set_.add(grid[i][j+1])
                set_.add(grid[i+1][j-1])
                set_.add(grid[i-1][j+1])
                
                for ind in set_:
                    if ind > 9 or ind < 1:
                        sums.add(19)
                        sums.add(20)
                if len(sums) == 1 and len(set_) == 9:
                    ctr += 1
        return ctr