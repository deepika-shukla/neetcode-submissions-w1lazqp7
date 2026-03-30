class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            area = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1)
            return area

        ans =0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 1:
                    area = dfs(i,j)
                    if area > ans:
                        ans = area
        return ans