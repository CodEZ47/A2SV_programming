class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)

        def solve(num):
            if num == 0:
                return 1
            
            if num < 0:
                return - 1
            
            if num in memo:
                return memo[num]
            
            s = 0

            for n in nums:
                temp = solve(num - n)
                if temp > 0:
                    s += temp
                
            memo[num] = s

            return memo[num]


        return solve(target)