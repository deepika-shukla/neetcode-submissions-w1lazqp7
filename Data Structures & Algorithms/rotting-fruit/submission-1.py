class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q =deque()
        visit = set()

        for r in range(len(grid)):
            for c in range((len(grid[0]))):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr,dc in directions:
                    r,c = row+dr, col+dc

                    if r in range(len(grid)) and c in range(len(grid[0])) and (r,c) not in visit and grid[r][c] == 1:
                        grid[r][c] == 2
                        fresh -= 1
                        q.append((r,c))
                        visit.add((r,c))
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time
            

        
