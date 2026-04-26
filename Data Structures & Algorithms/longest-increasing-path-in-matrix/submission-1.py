class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        dp = {} # (r,c) = max_path

        def dfs(r,c, preval):
            
            if r not in range(rows) or c not in range(cols) or matrix[r][c] <= preval:
                    return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            for dr, dc in directions:
                row, col = dr+r, dc+c
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r,c,float("-inf")))
        return longest


