class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t_dict = Counter(text)
        
        b = t_dict['b']
        a = t_dict['a']
        l = t_dict['l']//2
        o = t_dict['o']//2
        n = t_dict['n']
        
        return min(b,a,l,o,n)
            