class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr_str = 0
        ptr_end = len(s)-1
        
        while ptr_str < ptr_end:
            temp = s[ptr_str]
            s[ptr_str] = s[ptr_end]
            s[ptr_end] = temp
            ptr_str += 1
            ptr_end -= 1
        