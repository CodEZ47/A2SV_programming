class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)
        
        for value in nums_dict.values():
            if value > 1:
                return True
            
        return False