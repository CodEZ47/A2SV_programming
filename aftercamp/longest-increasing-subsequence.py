class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        long_sub = []


        for num in nums:
            idx = bisect.bisect_left(long_sub, num)
            if len(long_sub)-1 < idx:
                long_sub.append(num)
            elif long_sub[idx] != num:
                long_sub[idx] = num
            
        return len(long_sub)