class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = [value, k]
        self.dict = defaultdict(int)
        self.q = deque()
        return

    def consec(self, num: int) -> bool:
        if len(self.q) < self.stream[1]:
            self.q.append(num)
            # print(self.q)
            self.dict[num] += 1
            if self.dict[self.stream[0]] == self.stream[1]:
                return True
            return False
        
        self.dict[self.q[0]] -= 1
        self.q.popleft()
        self.q.append(num)
        self.dict[num] += 1

        if self.dict[self.stream[0]] == self.stream[1]:
            return True
        return False
        



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)