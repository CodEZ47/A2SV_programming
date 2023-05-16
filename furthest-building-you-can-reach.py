class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(1,len(heights)):
            curr_gap = heights[i] - heights[i-1]
            if curr_gap > 0:
                if len(heap) == ladders:
                    heapq.heappush(heap,curr_gap)
                    bricks -= heapq.heappop(heap)
                else:
                    heapq.heappush(heap,curr_gap)
            
            if bricks < 0:
                return i-1
        
        return len(heights)-1