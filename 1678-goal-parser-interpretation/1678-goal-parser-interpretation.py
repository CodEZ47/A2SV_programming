class Solution:
    def interpret(self, command: str) -> str:
        char_stk = []
        ans = ""
        
        for char in command:
            char_stk.append(char)
            
        while char_stk:
            if char_stk[-1] == "G":
                ans += char_stk.pop()
                continue
            if char_stk[-1] == ")":
                char_stk.pop()
                
                if char_stk[-1] == "(":
                    ans += "o"
                    char_stk.pop()
                    continue
                    
                while char_stk[-1] != "(":
                    ans += char_stk.pop()
                char_stk.pop()
                
        return ans[::-1]   