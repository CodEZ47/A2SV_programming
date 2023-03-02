class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for p in s:
            if p == "(":
                stk.append("(")
            else:
                if stk and stk[-1] == "(":
                    stk.pop()
                    val = 1
                elif stk:
                    val = stk.pop()
                    stk.pop()
                    val *= 2
                if stk and stk[-1] != "(":
                    stk.append(stk.pop() + val)
                else:
                    stk.append(val)
            print(stk)
        
        return stk.pop()