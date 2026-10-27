class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                position = (r*n+c+k)%(m*n)
                result[position//n][position%n] = grid[r][c]
        return result
