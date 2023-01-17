class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ind_max = 0
        rng = len(heights)
        
        for i in range(rng):
            ind_max = i
            for j in range(i+1, rng):
                if heights[j] > heights[ind_max]:
                    ind_max = j

            heights[ind_max], heights[i] = heights[i], heights[ind_max]
            names[ind_max], names[i] = names[i], names[ind_max]
        
        # print(heights)
        return names
        
        