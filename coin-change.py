class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = defaultdict(int)

        def solve(num):
            if num == 0:
                return 0
            
            if num < 0:
                return - 1
            
            if num in memo:
                return memo[num]
            
            mini = sys.maxsize

            for n in coins:

                temp =  solve(num - n)
                if temp >= 0:
                    mini = min(mini, temp)
            
            if mini == sys.maxsize:
                memo[num] = -1
                return memo[num]
            memo[num] = mini + 1
            return memo[num]

        return solve(amount)