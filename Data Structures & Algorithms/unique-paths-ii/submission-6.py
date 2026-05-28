class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*(m+1)
        # edge case
        dp[m-1] = 1

        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] = dp[c] + dp[c+1]
        return dp[0]
