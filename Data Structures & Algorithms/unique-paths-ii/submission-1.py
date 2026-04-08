class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # row,col = len(obstacleGrid), len(obstacleGrid[0])

        # dp = [0] * col
        # dp[-1] = 1

        # for r in range(row-1,-1,-1):
        #     for c in range(col-1,-1,-1):
        #         if obstacleGrid[r][c] == 1:
        #             dp[c] = 0
        #         elif c+1 < col:
        #             dp[c] = dp[c+1] + dp[c]
        # return dp[0]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ############ RECUSRIVE BRUTE FORCE
        # def backtrack(i,j):
        #     if i == m or j == n:
        #         return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     return backtrack(i+1,j) + backtrack(i, j+1)
        # return backtrack(0,0)

        dp = {} # (i,j) : count        
        def backtrack(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == m or j == n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            dp[(i,j)] = backtrack(i+1,j) + backtrack(i, j+1)
            return dp[(i,j)]
        return backtrack(0,0)





