class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        l, r = 0, len(self.timemap[key])-1
        t = self.timemap[key]
        print(t)
        res = ""
        while l <= r:
            m = (l+r)//2

            if t[m][1] <= timestamp:
                res = t[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
