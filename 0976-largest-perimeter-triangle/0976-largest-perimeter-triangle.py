class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        nums_len = len(nums)
        ptr = 0
        max = 0
        
        while ptr < nums_len - 2:
            a = nums[ptr]
            b = nums[ptr + 1]
            c = nums[ptr + 2]
            if a + b > c and a + c > b and c + b > a and a + b + c > max:
                max = a + b + c
            ptr += 1
            
        return max