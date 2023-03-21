class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(m, n):
            if n == 0:
                return 1
            if n < 0:
                m = 1/m
                n = -n
            if n % 2 == 0: 
                return calc(m*m, n//2)
            else:
                return m*calc(m*m, n//2)

        return calc(x,n)