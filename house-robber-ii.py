class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        def solve(n,s):
            if n in memo:
                return memo[n]
            if n >= size:
                return 0
            if n == size-1 and s == 0:
                return 0
            
            memo[n] = max(solve(n+2,s),solve(n+3,s)) + nums[n]

            return memo[n]
        
        if size < 3:
            return max(nums)
        maxi = 0
        for i in range(size):
            memo = defaultdict(int)
            maxi = max(solve(i,i),maxi)
        
        return maxi