class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.i = 0
        self.summ = 0
        self.size = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.i += 1
        self.summ += val
        if self.i > self.size:
            prev = self.q.popleft()
            self.summ -= prev
            self.i -= 1
        return self.summ / self.i

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
