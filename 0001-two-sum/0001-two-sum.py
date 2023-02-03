class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for index,n in enumerate(nums):
            if target - n in nums_dict:
                return[index,nums.index(target - n)]
            nums_dict[n] = index
        