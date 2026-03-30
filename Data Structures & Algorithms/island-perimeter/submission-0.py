class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 1
            if grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0

            visit.add((r, c))
            perimeter = 0
            for dr, dc in directions:
                perimeter += dfs(r + dr, c + dc)
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
