class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        rows, cols = len(grid), len(grid[0])
        maxarea = 0
        visit = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r,c): # return area
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            area = 1 # starting with this node, area will be 1
            for dr, dc in directions:
                row, col = r+dr, c+dc
                area += dfs(row, col)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxarea = max(maxarea, dfs(r,c))
        return maxarea


        # BFS

        rows, cols = len(grid), len(grid[0])
        maxarea = 0
        visit = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            while q:
                r,c = popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row not in range(rows) or col not in range(cols) or grid[row][col] == 0 or (row,col) in visit:
                        continue
                    visit.add((row,col))
                    q.append((row,col))
                    area+=1
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxarea = max(maxarea, bfs(r,c))
        return maxarea