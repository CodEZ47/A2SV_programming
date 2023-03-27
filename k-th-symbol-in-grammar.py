class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def rec(n,k):
            if n == 1:
                return 0
            
            prev = rec(n-1, ceil(k/2))
            flag = (k % 2 == 1)

            if prev == 1:
                if flag:
                    return 1
                return 0
            else:
                if flag:
                    return 0
                return 1
        
        return rec(n,k)