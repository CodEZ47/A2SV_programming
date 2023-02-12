class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst = []
        row = len(matrix)
        col = len(matrix[0])
        
        for j in range(col):
            for i in range(row-1, -1,-1):
                lst.append(matrix[i][j])
        
        n = row * col
        
        # print(lst)
        for i in range(n):
            x = i // col
            y = i % col
            
            matrix[x][y] = lst[i]
            
        
        