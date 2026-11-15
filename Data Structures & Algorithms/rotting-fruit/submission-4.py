class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        count = 0
        while q and fresh > 0: # only do when we have fresh
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r,c = row+dr, col+dc

                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    
                    grid[r][c] = 2
                    fresh -= 1
                    
                    q.append((r,c))

            
            count += 1
        
        return -1 if fresh != 0 else count

