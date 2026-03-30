class FreqStack:

    def __init__(self):
        self.stack = {}
        self.maxCount = 0
        self.freq = {}

    def push(self, val: int) -> None:
        self.stack[val] = 1 +  self.stack.get(val, 0)
        if self.stack[val] > self.maxCount:
            # we found the new maximum
            self.maxCount = self.stack[val]
            self.freq[self.stack[val]]  = []
        self.freq[self.stack[val]].append(val)       

    def pop(self) -> int:
        res =  self.freq[self.maxCount].pop()
        # reduce the count
        self.stack[res] -= 1
        if not self.freq[self.maxCount]:
            self.maxCount -= 1
        return res


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()