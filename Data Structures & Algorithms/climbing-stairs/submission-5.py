class Solution:
    def climbStairs(self, n: int) -> int:
        # # bruteforce 

        # def dfs(i):
        #     if i == n:
        #         return 1
            
        #     if i > n:
        #         return 0
            
        #     steps = dfs(i+1) + dfs(i+2)
        #     return steps
        # return dfs(0)

        # memoization -  top-down

        cache = {}
        def dfs(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            if i in cache:
                return cache[i]
            
            steps = dfs(i+1) + dfs(i+2)
            cache[i] = steps
            return steps
        return dfs(0)