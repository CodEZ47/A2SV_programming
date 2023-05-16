class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        ans = []

        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
        vis = set()
        vis.add((0,0))

        def inRange(coord):
            return coord[0] < len(nums1) and coord[1] < len(nums2)

        while k and heap:
            temp = heapq.heappop(heap)
            l = temp[1]
            r = temp[2]
            ans.append([nums1[l],nums2[r]])

            if (l+1,r) not in vis and inRange((l+1,r)):
                heapq.heappush(heap, (nums1[l+1] + nums2[r], l+1, r))
                vis.add((l+1,r))
            if (l,r+1) not in vis and inRange((l,r+1)):
                heapq.heappush(heap, (nums1[l] + nums2[r+1], l, r+1))
                vis.add((l,r+1))
            
            k -= 1
        
        return ans