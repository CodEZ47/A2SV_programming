class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n        
        ans = self.fib(n-1) + self.fib(n-2)
        return ans