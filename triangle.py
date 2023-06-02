class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        size = len(triangle)
        memo = defaultdict(int)
        # print(size)
        def solve(i,lvl):
            if lvl >= size:
                return 0
            if (i,lvl) in memo:
                return memo[(i,lvl)]
            
            a = solve(i,lvl+1)
            b = solve(i+1,lvl+1)
            # print(a,b,i,lvl)

            memo[(i,lvl)] = min(a,b) + triangle[lvl][i]

            return memo[(i,lvl)]
        
        return solve(0,0)