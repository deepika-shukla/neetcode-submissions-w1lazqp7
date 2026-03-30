class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row,col = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * col
        dp[-1] = 1

        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c+1 < col:
                    dp[c] = dp[c+1] + dp[c]
        return dp[0]






