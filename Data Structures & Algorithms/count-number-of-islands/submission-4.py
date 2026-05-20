class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # we need to find the 1 and mark all its neighbour
        # rows, cols = len(grid), len(grid[0])
        # island = 0
        # visit = set()
        # directions = [(1,0), (0,1), (-1,0), (0,-1)]
        # def dfs(row,col):
        #     if row not in range(rows) or col not in range(cols) or grid[row][col] == "0" or (row, col) in visit:
        #         return
        #     visit.add((row,col))
        #     for dr, dc in directions:
        #         r, c = row+dr, col + dc 
        #         dfs(r,c)

            
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             dfs(r,c)
        #             island += 1
        # return island

        # BFS
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row not in range(rows) or col not in range(cols)or (row, col) in visit or grid[row][col] == "0"):
                        continue

                    visit.add((row,col))
                    q.append((r+dr, c+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        return island
