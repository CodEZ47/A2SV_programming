class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_len = len(heights)
        is_sorted = False
        temp = ""
        
        while not is_sorted:
            is_sorted = True
            
            for i in range(h_len-1):
                if heights[i] < heights[i+1]:
                    temp = names[i]
                    names[i] = names[i+1]
                    names[i+1] = temp
                    temp = heights[i]
                    heights[i] = heights[i+1]
                    heights[i+1] = temp
                    is_sorted = False
        
        print(names)
        return names