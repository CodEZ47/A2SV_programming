class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_len = len(nums)
        ctr = 0
        
        for i in range(nums_len):
            for j in range(nums_len):
                if nums[i] == nums[j] and i < j:
                    ctr += 1
        print(ctr)
        return ctr