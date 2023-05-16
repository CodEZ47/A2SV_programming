class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        self.ctr = 0

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small,num*-1)
        elif num > self.small[0] * -1:
            if len(self.large) < len(self.small):
                heapq.heappush(self.large,num)
            else:
                heapq.heappush(self.large,num)
                temp = heapq.heappop(self.large)
                heapq.heappush(self.small,temp*-1)
        
        else:
            if len(self.small) < len(self.large)+1:
                heapq.heappush(self.small,num*-1)
            else:
                temp = heapq.heappop(self.small) * -1
                heapq.heappush(self.large, temp)
                heapq.heappush(self.small,num*-1)
        
        self.ctr += 1

        
    def findMedian(self) -> float:

        if self.ctr % 2:
            return self.small[0] * -1
        return ((self.small[0] * -1) + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()