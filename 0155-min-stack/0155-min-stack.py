class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val < self.min[-1]:
            self.min.append(val)
            return
        self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()