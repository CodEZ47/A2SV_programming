class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        vis = set()
        
        def chk(row,col):
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])
        
        
        
        
        curr = image[sr][sc]
        
        def dfs(img, row, col, vis):            
            if not chk(row,col) or img[row][col] != curr:
                return
            
            if img[row][col] == curr:
                img[row][col] = color
                
            vis.add((row,col))
            
            for neigh in direction:
                new_row = row + neigh[0]
                new_col = col + neigh[1]
                
                
                if (new_row, new_col) not in vis:
                    dfs(img,new_row,new_col,vis)
        
        
        dfs(image,sr,sc,vis)
            
        
        return image