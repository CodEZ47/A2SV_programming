class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars = defaultdict(str)
        chars2 = defaultdict(str)

        n = len(s)

        for i in range(n):
            if t[i] in chars and chars[t[i]] != s[i]:
                return False
            else:
                chars[t[i]] = s[i]
        for i in range(n):
            if s[i] in chars2 and chars2[s[i]] != t[i]:
                return False
            else:
                chars2[s[i]] = t[i]
        
        
        return True