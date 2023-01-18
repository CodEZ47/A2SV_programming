class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        diff_dict = {}
        
        for i in range(row):
            for j in range(col):
                temp = i - j
                if temp in diff_dict:
                    if diff_dict[temp] != matrix[i][j]:
                        return False
                else:
                    diff_dict[temp] = matrix[i][j]
        
        return True