class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = Counter(s)
        td = Counter(t)

        if sd == td:
            return True
        
        return False