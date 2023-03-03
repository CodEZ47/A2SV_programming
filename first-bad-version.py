# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        last_bad = 0

        while l <= r:
            # print(l, r)
            mid = l + (r-l) // 2
            isBad = isBadVersion(mid)
            if isBad:
                last_bad = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return last_bad