class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(r,c):
            # edge cases
            if r not in range(m) or c not in range(n):
                return 0 # we didn't find path
            
            # found the path
            if r == m-1 and c == n-1:
                return 1

            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            
            return cache[(r,c)]
        return dfs(0,0)