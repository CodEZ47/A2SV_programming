class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)/2
        
        nums.sort()
        
        ctr = 1
        num = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] == num:
                ctr += 1
                continue
                
            if ctr > m:
                return num
            else:
                ctr = 1
                num = nums[i]
        
        return num