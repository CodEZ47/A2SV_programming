class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        new_arr = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                new_arr.append(i)
        
        return new_arr