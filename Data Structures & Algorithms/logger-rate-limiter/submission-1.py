class Logger:

    def __init__(self):
        self.store = {} # key, with timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.store:
            self.store[message] = 10 + timestamp
            return True

        if self.store[message] > timestamp:
            return False
        self.store[message] = 10 + timestamp
        return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
