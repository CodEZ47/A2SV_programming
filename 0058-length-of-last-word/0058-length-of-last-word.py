class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ctr = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                ctr += 1
                continue
            if s[i] == " " and ctr > 0:
                break
        
        return ctr