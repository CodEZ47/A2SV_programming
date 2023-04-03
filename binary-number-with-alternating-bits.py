class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n = n >> 1
        while n:
            curr = n & 1
            if prev == curr:
                return False
            n = n >> 1
            prev = curr
        
        return True