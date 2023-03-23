class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        r_sum = 0
        r_dict = Counter()
        r_dict[0] = 1
        ans = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            ans += r_dict[r_sum - goal]
            r_dict[r_sum] += 1
        
        return ans