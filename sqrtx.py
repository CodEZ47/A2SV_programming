class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (l+r) >> 1

            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x and (mid+1)*(mid+1) > x:
                return mid
            else:
                l = mid + 1
        
        return r