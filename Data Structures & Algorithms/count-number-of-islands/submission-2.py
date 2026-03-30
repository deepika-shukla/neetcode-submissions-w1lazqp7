class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        #DFS solution
        visit = set()
        island = 0
        def islands(i, j):
            if (i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0' or (i,j) in visit):
                return
            
            visit.add((i,j))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for d1,d2 in directions:
                r,c = i+d1, j+d2
                islands(r,c)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands(r,c)
                    island += 1
        return island

            

        #BFS solution