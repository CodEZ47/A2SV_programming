class DetectSquares:

    def __init__(self):
        self.ctr = defaultdict(int)
        self.points = set()

    def add(self, point):
        x, y = point
        self.ctr[(x, y)] += 1
        self.points.add((x, y))

    def count(self, point):
        x, y = point
        ans = 0
        for px, py in self.points:
            if px != x and py != y and abs(px - x) == abs(py - y):
                ans += self.ctr[(x, py)] * self.ctr[(px, y)] * self.ctr[(px, py)]
        return ans

        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)