class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mnmum = 1000000
        lst_len = len(points)
        temp = 0
        curr_ind = -1
        
        for ind in range(lst_len):
            
            if(points[ind][0] == x or points[ind][1] == y):
                
                temp = abs(x - points[ind][0]) + abs(y - points[ind][1])
                print(temp)
                
                if temp < mnmum:
                    mnmum = temp
                    curr_ind = ind
                    temp = 0
                    
        return curr_ind
        