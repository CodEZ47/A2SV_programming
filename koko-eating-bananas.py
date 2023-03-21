class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def chk(speed):
            tt = 0
            for p in piles:
                tt += ceil(p/speed)
            if tt > h:
                return False
            return True

        l,r = 1, max(piles)
        while l < r:
            mid = (l+r) >> 1

            if chk(mid):
                r = mid
            else:
                l = mid + 1

        return l