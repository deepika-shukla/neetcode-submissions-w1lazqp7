class MyQueue:

    def __init__(self):
        # we will use two stack
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # append in stack1
        self.stack1.append(x)
        

    def pop(self) -> int:
        # when we pop, first pop from stack 1 store in stack 2
        # then pop because we need first element to pop
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        a = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return a
        

    def peek(self) -> int:
        # same logic here
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        a = self.stack1[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return a

    def empty(self) -> bool:
        if not self.stack1:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()