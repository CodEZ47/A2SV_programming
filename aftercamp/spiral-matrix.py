class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        n = (row) * (col)
        ind = [0,0]
        prev = [0,0]
        output = []
        
        l = 0
        t = 0
        r = col - 1
        b = row - 1
        
        if col == 1:
            for i in range(row):
                output.append(matrix[i][0])
            return output
        
        if row == 1:
            return matrix[0]
        
        
        while n > 0:
            if ind == [t, l]:
                print(1)
                while ind != [t, r] and n > 0:
                    output.append(matrix[ind[0]][ind[1]])
                    n -= 1
                    ind[1] += 1
                t += 1   
                print(output)
                continue
        
            if ind == [t-1, r]:
                print(2)
                while ind != [b, r] and n > 0:
                    output.append(matrix[ind[0]][ind[1]])
                    n -= 1
                    ind[0] += 1
                r -= 1
                print(output)
                continue
               
            if ind == [b, r+1]:
                print(3)
                while ind != [b, l] and ind[1] > 0 and n > 0:
                    output.append(matrix[ind[0]][ind[1]])
                    n -= 1
                    ind[1] -= 1
                l += 1
                print(output)
                continue
                
            if ind == [b, l-1]:
                print(4)
                while ind != prev and ind[0] > 0 and n > 0:
                    output.append(matrix[ind[0]][ind[1]])
                    n -= 1
                    ind[0] -= 1
                b -= 1
                print(output)
                
            ind = [t,l]
            prev[0] += 1
            prev[1] += 1
            # print(output)
            # break
            
        return output
                
                