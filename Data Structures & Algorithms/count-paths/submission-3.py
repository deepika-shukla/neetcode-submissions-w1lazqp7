class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ###########3 RECUSRIVE [BRUTE FORCE]
        # def backtrack(i, j):
        #     if i == m or j == n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     return backtrack(i+1, j) + backtrack(i, j+1)
        # return backtrack(0,0)


        ############3 MEMOIZATION

        dp = {} # (i,j) : count

        def backtrack(i,j):
            if (i, j) in dp:
                return dp[(i,j)]
            if i == m or j == n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            dp[(i,j)] = backtrack(i+1, j) + backtrack(i, j+1)
            return dp[(i,j)]
        return backtrack(0,0)
