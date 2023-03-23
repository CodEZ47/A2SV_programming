class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def rec(n = n):
            if n == 0:
                return "0"
            
            newS = rec(n-1)
            inv = []

            for char in newS:
                if char == "0":
                    inv.append("1")
                else:
                    inv.append("0")
            
            inv.reverse()
            inv = "".join(inv)
            return newS + "1" + inv
        
        ans = list(rec())

        return ans[k-1]