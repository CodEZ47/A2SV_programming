class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat        
        
        flat_list = [i for l in mat for i in l]
        ans = [[0]*c for i in range(r)]
        
        for i in range(len(flat_list)):
            x = i // c
            y = i % c
            
            ans[x][y] = flat_list[i]
        
        
        return ans