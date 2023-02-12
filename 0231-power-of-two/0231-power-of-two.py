class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 0
        i = 0
        while m <= n:
            m = pow(2,i)
            if m == n:
                return True
            i += 1
        return False
        