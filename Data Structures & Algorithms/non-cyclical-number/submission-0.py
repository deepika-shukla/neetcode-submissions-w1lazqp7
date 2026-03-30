class Solution:

    def sum_of_sqaures(self,n):
        s = 0
        while n > 0:
            digit = n % 10
            s += digit**2
            n = n // 10
        return s

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n >= 1:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.sum_of_sqaures(n)
