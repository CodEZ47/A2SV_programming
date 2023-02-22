class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        n = 0
        max_ = 0
        prev = 0
        temp = 0
        print(nums)
        for i in range(len(nums)):
            while n < len(nums) and nums[i] - nums[n] <= k:
                k -= (nums[i] - nums[n])
                max_ = max(max_,(n-i+1))
                prev = n
                n += 1
            if i<len(nums)-1:
                k += (nums[i]-nums[i+1])*(prev-i)
            

        return max_;