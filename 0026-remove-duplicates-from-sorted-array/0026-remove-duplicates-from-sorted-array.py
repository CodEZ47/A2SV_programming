class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
        temp = nums[0]
        
        while r < len(nums):
            if nums[r] > temp:
                temp = nums[r]
                nums[r], nums[l] = nums[l], nums[r]
                r += 1
                l += 1
                continue
            r += 1
        
        # print(nums)
        # print(l)
        return l