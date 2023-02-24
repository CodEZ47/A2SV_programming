class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        
        stack = "".join(stack)
        
        return stack