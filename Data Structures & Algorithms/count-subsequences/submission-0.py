class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # edge case
        if len(t) > len(s):
            return 0
            
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            ans = dfs(i+1,j) # we always need to move forward in s
            if s[i] == t[j]:
                ans += dfs(i+1, j+1)
            return ans
        return dfs(0, 0)
            