class Solution:
    def count(self, n):
        c = 0
        while n:
            n &=(n-1)
            c += 1
        return c

    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            l.append(self.count(i))
        return l
