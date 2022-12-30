class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)
        
        for ind in range(nums_len):
            if nums[ind] != ind:
                return ind
        return nums_len