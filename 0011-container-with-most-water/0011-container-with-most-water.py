class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        s = 0
        e = len(height)-1
        
        while s <= e:
            temp = (e - s) * min(height[s], height[e])
            if temp > max_area:
                max_area = temp
            
            if height[s] >= height[e]:
                e -= 1
            else:
                s += 1
        
        return max_area