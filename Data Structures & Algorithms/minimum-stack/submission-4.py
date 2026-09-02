class MinStack:

    def __init__(self):
        self.min = float("-inf")
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # the only value
            self.stack.append(0)
            self.min= val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        last = self.stack.pop()
        if last < 0:
            # we need to update smallest
            self.min = self.min - last
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0 :
            return top + self.min
        else:
            return self.min # that would be min value itself

    def getMin(self) -> int:
        return self.min
