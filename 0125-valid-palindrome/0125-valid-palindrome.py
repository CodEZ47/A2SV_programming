class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        
        s = s.lower()
        for char in s:
            if char.isalnum():
                lst.append(char)
        
        s = "".join(lst)
        lst.reverse()
        s_rev = "".join(lst)
        
        # print(s, s_rev)
        
        if s == s_rev:
            return True
        else:
            return False