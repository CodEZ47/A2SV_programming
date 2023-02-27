class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dict_let = defaultdict(int)
        max_wind = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            if s[i] in dict_let:
                while s[l] != s[i]:
                    dict_let.pop(s[l])
                    l += 1
                if l < i:
                    l += 1
                continue
            
            dict_let[s[i]] += 1
            max_wind = max(max_wind, i - l+1)
            # print(s[i], dict_let[s[i]])
        
        return max_wind
                