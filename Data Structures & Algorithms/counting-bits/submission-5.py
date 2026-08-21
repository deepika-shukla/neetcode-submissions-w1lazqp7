class Solution:
    def bits(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            l.append(self.bits(i))
        return l
        