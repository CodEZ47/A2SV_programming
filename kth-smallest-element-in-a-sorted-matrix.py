class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heap.append(matrix[i][j])
        
        heapq.heapify(heap)

        ans = 0
        for i in range(k):
            ans = heapq.heappop(heap)
        
        return ans