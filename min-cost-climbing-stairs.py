class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = defaultdict(int)


        def solve(idx):
            # print(idx,memo)
            if idx >= len(cost):
                return 0
            if idx in memo:
                return memo[idx]
            # print(idx)
            
            mini = min(solve(idx+1),solve(idx+2))
            
            memo[idx] = mini + cost[idx]
            # print(memo)
            return memo[idx]
        

        return min(solve(0), solve(1))