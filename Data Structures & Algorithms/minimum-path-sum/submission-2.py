class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        n,m = len(grid),len(grid[0])
        dp[n-1][m-1] = grid[n-1][m-1]

        for r in range(n-1, -1,-1):
            for c in range(m-1, -1, -1):
                if r == n-1 and c == m-1:
                    continue
                else:
                    dp[r][c] = grid[r][c] + min(dp[r][c+1],dp[r+1][c] )
        return dp[0][0]