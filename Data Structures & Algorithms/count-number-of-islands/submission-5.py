class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in visit or grid[i][j] == "0":
                return
            visit.add((i,j))

            for dr, dc in directions:
                dfs(i+dr, j+dc)


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    island += 1
        return island
            
             