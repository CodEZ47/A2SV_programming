class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        rng = len(heights)
        max_h = max(heights)+1
        
        arr = [0]*max_h
        
        for i in range(rng):
            arr[heights[i]] = names[i]
        
        final_arr = []
        
        for val in arr:
            if val != 0:
                final_arr.append(val)
        
        final_arr.reverse()
        print(arr)
        return final_arr
            
        