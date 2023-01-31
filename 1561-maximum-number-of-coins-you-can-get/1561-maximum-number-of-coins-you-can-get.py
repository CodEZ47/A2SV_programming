class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n = len(piles)/3
        n = int(n)
        s = 0
        
        for i in range(n):
            piles.pop()
            s += piles[-1]
            piles.pop()
        
        return s