class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m = len(num)
        m = pow(10, m-1)
        ans = 0
        
        for i in range(len(num)):
            if i == 0:
                ans += m * num[i]
            else:
                m = m // 10
                ans += m * num[i]
        
        ans += k
        res = []
        
        while ans > 0:
            res.append(ans % 10)
            ans = ans // 10
        
        res.reverse()
        return res