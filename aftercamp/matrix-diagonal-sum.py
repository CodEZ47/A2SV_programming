class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        m = len(mat[0])

        if n == 1:
            return mat[0][0]

        vis = set()

        i = 0
        j = 0

        while i < n and j < m:
            s += mat[i][j]
            i += 1
            j += 1

            vis.add((i,j))
        
        i = 0
        j = m-1

        while i < n and j > -1:
            if (i,j) not in vis:
                s += mat[i][j]
                vis.add((i,j))

            i += 1
            j -= 1

        return s