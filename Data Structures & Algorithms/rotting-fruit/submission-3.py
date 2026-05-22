class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        fresh = 0
        time = 0 
        q = deque()
        visit = set()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
            

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in visit and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))
                        visit.add((row,col))
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time
