class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_arr = [0]*len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    new_arr[i] += 1
        return new_arr
                    