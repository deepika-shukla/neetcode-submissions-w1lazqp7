class Solution:
    # def count(self, n):
    # #     c = 0
    # #     while n:
    # #         n &=(n-1)
    # #         c += 1
    # #     return c

    def countBits(self, n: int) -> List[int]:
        # l = []
        # for i in range(n+1):
        #     l.append(self.count(i))
        # return l

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
