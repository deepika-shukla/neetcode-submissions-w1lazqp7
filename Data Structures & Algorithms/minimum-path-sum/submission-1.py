class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # recurisve
        rows, cols = len(grid), len(grid[0])
        
        # def dfs(r,c):
        #     if r == rows or c == cols:
        #         # we wnt out of range
        #         return float('inf')
        #     if r == rows-1 and c == cols -1:
        #         # we reach the last point
        #         return grid[r][c]
            
        #     # now we can either go right or down
        #     right = dfs(r, c+1)
        #     down = dfs(r+1, c)

        #     # we need to take the minimum path
        #     return grid[r][c] + min(down, right)
            
        
        # return dfs(0,0)


        # memo

        memo = {}

        def dfs(r,c):
            if r == rows -1 and c == cols - 1:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            if r == rows or c == cols:
                return float("inf")
            
            right = dfs(r+1, c)
            down = dfs(r, c+1)

            memo[(r,c)] = grid[r][c] + min(right, down)
            return memo[(r,c)]
        return dfs(0,0)
                
