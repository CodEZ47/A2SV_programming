class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)
        s = sum(nums)

        def solve(idx,total):
            if idx >= len(nums):
                if total == target:
                    return 1
                return 0
            
            if (total,idx) in memo:
                return memo[(total,idx)]


            s = 0

            s += solve(idx+1,total + nums[idx])
            s += solve(idx+1,total - nums[idx])

            memo[(total,idx)] = s

            return memo[(total,idx)]
            
        

        return solve(0,0)