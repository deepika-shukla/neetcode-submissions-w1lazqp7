class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we will use 2dp : bottom up approach

        prevrow = [0] * n

        for i in range(m-1,-1,-1):
            currow = [0] * n
            currow[n-1] = 1 # last index, only one way to reach
            for j in range(n-2,-1,-1):
                currow[j] = currow[j+1] + prevrow[j]
            prevrow = currow
        return currow[0]
 