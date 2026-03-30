class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        islands = 0

        def dfs(r,c):
            if ( r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == "0"):
                return
            visit.add((r,c))
            #run function for its neighbour
            directions= [[1,0], [0,1], [-1, 0], [0,-1]]
            for dr, dc in directions:
                row, col = r+dr, c + dc
                dfs(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands


        