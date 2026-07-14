class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # from each index we can compute the path
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        longest = 0
        #cache
        dp = {}

        def dfs(r,c, preval):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= preval:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1 # preval count
            for dr, dc in directions:
                row, col = dr+r, dc+c
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r,c,float("-inf")))
        return longest


