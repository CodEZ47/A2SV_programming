class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        dig_sum = 0
        
        for num in nums:
            while num:
                dig_sum += num % 10
                num = num // 10
        
        
        return abs(elem_sum - dig_sum)