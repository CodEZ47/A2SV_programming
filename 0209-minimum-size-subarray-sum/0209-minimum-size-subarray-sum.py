class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot, p1, p2 = 0,0,0
        length = 1
        sum_ = nums[0]
        min_ = 100000

        tot = sum(nums)

        if tot < target:
            return 0

        while p2 < len(nums) and p1 < len(nums):
            
            if p1 == p2 and sum_ >= target:
                return 1

            if sum_ >= target and p1 < p2:
                if length < min_:
                    min_ = min(min_,length)
                sum_ -= nums[p1]
                p1 += 1
                length -= 1
                continue

            length += 1
            p2 += 1
            if p2 < len(nums):
                sum_ += nums[p2]

        return min_