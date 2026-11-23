class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # brute force
        # rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # def dfs(r,c):
        #     if r not in range(rows) or c not in range(cols):
        #         return 0
        #     if obstacleGrid[r][c] == 1:
        #         return 0
        #     if r == rows-1 and c == cols - 1:
        #         return 1
            
        #     return dfs(r+1, c) + dfs(r, c+1)
        # return dfs(0,0)


        ################ top down( memoization)
        # cache = {}
        # rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # def dfs(r,c):
        #     if r not in range(rows) or c not in range(cols):
        #         return 0
        #     if obstacleGrid[r][c] == 1:
        #         return 0
        #     if r == rows-1 and c == cols - 1:
        #         return 1
        #     if (r,c) in cache:
        #         return cache[(r,c)]

        #     cache[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            
        #     return cache[(r,c)]
        # return dfs(0,0)

        ############# BOTTOM UP
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * (cols+1)
        dp[cols-1] = 1

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1]
        return dp[0]

                