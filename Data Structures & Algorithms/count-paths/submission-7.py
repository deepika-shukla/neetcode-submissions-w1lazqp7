class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ####### TOP DOWN ( memoization)
        # cache = {}
        # def dfs(r,c):
        #     # edge cases
        #     if r not in range(m) or c not in range(n):
        #         return 0 # we didn't find path
            
        #     # found the path
        #     if r == m-1 and c == n-1:
        #         return 1

        #     if (r,c) in cache:
        #         return cache[(r,c)]

        #     cache[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            
        #     return cache[(r,c)]
        # return dfs(0,0)

        ######### BOTTOM UP 
        prev = [1] * n

        for r in range(m-1):
            cur = [1] * n
            for c in range(n-2,-1,-1):
                cur[c] = cur[c+1] + prev[c]
            prev = cur
        return prev[0]