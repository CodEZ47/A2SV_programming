class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [];
        s = lambda a,b: a+b
        d = lambda a,b: a-b
        m = lambda a,b: a*b
        div = lambda a,b: math.trunc(a/b)
        operators = {
            '+': s,
            '-': d,
            '*': m,
            '/': div
        }

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(operators[token](num1, num2))
            else:
                stack.append(int(token))

        return stack.pop()