class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t_dict = defaultdict(int)
        
        for ch in 'balon':
            t_dict[ch] = 0
            
        for ch in text:
            if ch in "balon":
                t_dict[ch] += 1
        
        t_dict['l'] //= 2
        t_dict['o'] //= 2 
        
        return min(t_dict.values())
            