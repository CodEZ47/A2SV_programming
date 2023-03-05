class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = 0
        dp = {0:1}
        ans = 0

        for num in nums:
            s += num
            key = s % k

            if key in dp:
                ans += dp[key]
                dp[key] += 1
            else:
                dp[key] = 1
        
        return ans