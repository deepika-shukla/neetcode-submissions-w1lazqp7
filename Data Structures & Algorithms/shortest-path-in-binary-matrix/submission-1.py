class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        q = deque() # r,c, length to reach the node
        visit = set()
        q.append((0,0,1))
        visit.add((0,0))
        directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]

        while q:
            row,col,path = q.popleft()
            if row == n-1 and col == n-1:
                return path
            for dr, dc in directions:
                r, c = row+dr, col + dc
                
                if r not in range(n) or c not in range(n) or grid[r][c] == 1 or (r,c) in visit:
                    continue
                q.append((r,c,path+1))
                visit.add((r,c))

        return -1