class StockSpanner:

    def __init__(self):
        self.stack = [] # store value and span

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        

        if self.stack and price < self.stack[-1][0]:
            self.stack.append([price, 1])
        else:     
            val = 1
            while self.stack and price >= self.stack[-1][0]:
                p, v = self.stack.pop()
                val += v
            self.stack.append([price, val])
        
        return self.stack[-1][1]
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)