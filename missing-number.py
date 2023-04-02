class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0

        while i < len(nums):
            temp = nums[i]

            if temp < len(nums) and temp != i:
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)