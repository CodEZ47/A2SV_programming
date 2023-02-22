class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = -10000
        
        l = 0
        r = 0
        sum_ = nums[0]
        
        if len(nums) == 1:
            return nums[0]/k
        if k == 1:
            return max(nums)
        
        while r < k-1:
            r += 1
            sum_ += nums[r]
            
        # print(sum_, r)
        max_ = max(max_, sum_/k)
        
        while r < len(nums)-1:
            r += 1
            sum_ += nums[r]
            sum_ -= nums[l]
            l += 1
            max_ = max(max_, (sum_/k))
        
        return max_
            