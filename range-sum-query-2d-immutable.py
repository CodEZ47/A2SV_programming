class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.m = [[0] * (c + 1) for i in range(r + 1)]

        for i in range(r):
            temp = 0
            for j in range(c):
                temp += matrix[i][j]
                self.m[i+1][j+1] = temp + self.m[i][j+1]
        
        print(self.m)
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot = self.m[row2+1][col2+1]
        diff = self.m[row1][col2+1] + self.m[row2+1][col1] - self.m[row1][col1]

        return tot -diff

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)