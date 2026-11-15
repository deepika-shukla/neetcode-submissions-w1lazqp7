class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0,0))
        visit = set()
        visit.add((0,0))

        directions = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1, -1], [-1,1]]

        path = 1

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == n-1 and c == n-1:
                    return path
                
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= n or col < 0 or col >=n or (row,col) in visit or grid[row][col] == 1:
                        continue
                
                    visit.add((row,col))
                    q.append((row, col))
            path += 1
        return -1



         