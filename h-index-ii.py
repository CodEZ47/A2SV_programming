class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        l = 0
        r = len(citations) - 1
        def chk(mid):
            return (citations[mid]) >= (len(citations) - mid)
        

        while (l < r):
            mid = (l+r) >> 1

            if chk(mid):
                r = mid
            
            else:
                l = mid + 1
        
        if citations[l] == 0:
            return 0

        return len(citations) - l