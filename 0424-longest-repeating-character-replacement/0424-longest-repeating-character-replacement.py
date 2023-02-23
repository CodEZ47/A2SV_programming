class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        ans = 0
        l = 0
        max_ = 0
        
        dict_ = defaultdict(int)
        
        for i in range(length):
            dict_[s[i]] += 1
            max_ = max(max_, dict_[s[i]])
            
            while ((i-l+1)-max_) > k:
                dict_[s[l]] -= 1
                l += 1
            
            ans = max(ans, i-l+1)
        
        return ans