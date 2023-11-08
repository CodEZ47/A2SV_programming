class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.s = 0

    def next(self, price: int) -> int:
        temp = []
        while self.stocks and self.stocks[-1][0] <= price:
            temp = self.stocks.pop()
        
        if temp:
            self.stocks.append([price,self.s, temp[2]])
        else:
            self.stocks.append([price,self.s, self.s])
        
        self.s += 1

        return self.stocks[-1][1] - self.stocks[-1][2] + 1




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)