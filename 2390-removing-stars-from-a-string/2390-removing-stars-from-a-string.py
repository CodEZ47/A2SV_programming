class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        
        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
                continue
            stack.append(s[i])
        
        stack = "".join(stack)
        
        return stack