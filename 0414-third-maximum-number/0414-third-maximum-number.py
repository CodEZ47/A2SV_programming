class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        nums_set = list(nums_set)
        nums_set.sort()
        
        if len(nums_set) < 3:
            return nums_set[-1]
        
        return nums_set[-3]