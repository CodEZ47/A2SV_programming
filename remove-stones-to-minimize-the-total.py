class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        
        heapq.heapify(piles)

        for i in range(k):
            temp = heapq.heappop(piles)
            temp = temp // 2
            heapq.heappush(piles,temp)
        
        return (sum(piles) * -1)