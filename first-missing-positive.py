class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            temp = nums[i] - 1

            if temp < len(nums) and temp > -1 and nums[temp] != nums[i]:
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1
        
        print(nums)

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        
        return len(nums)+1