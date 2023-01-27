class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = 0 
        a = 1
        
        while a > 0:
            a = c - (b*b)
            
            if a >= 0:
                sr = int(sqrt(a))
                if sr*sr == a:
                    return True
            b += 1
        return False