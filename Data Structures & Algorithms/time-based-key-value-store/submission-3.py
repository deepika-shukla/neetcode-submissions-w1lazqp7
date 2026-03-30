class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.d:
            return self.d[(key, timestamp)]
        while timestamp >= 1 and (key, timestamp) not in self.d:
            timestamp -= 1
        if timestamp < 1:
            return ""
        return self.d[(key, timestamp)]
