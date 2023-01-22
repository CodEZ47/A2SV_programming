class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        x = 0
        
        for i in range(row):
            if matrix[i][0] <= target and target <= matrix[i][col-1]:
                x = i
                break
        for y in range(col):
            if matrix[x][y] == target:
                return True
        
        return False