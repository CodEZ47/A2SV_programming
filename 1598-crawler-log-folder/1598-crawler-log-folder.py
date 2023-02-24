class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for op in logs:
            if op == "../" and stack:
                stack.pop()
            if op != "./" and op != "../":
                stack.append(op)
                
        return len(stack)