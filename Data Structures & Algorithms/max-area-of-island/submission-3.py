class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(r, c):
            # bounds / visited / water checks
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            area = 1
            for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                area += dfs(r + dr, c + dc)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
        return max_area
        # BFS