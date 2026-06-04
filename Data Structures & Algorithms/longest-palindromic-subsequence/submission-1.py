class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     return self.longestCommonSubseq(s, s[::-1])
    
    # def longestCommonSubseq(self, a,b):
    #     dp = [[0]* (len(b)+1) for h in range(len(a) + 1) ]

    #     for i in range(len(a)-1,-1,-1):
    #         for j in range(len(b)-1,-1,-1):
    #             if a[i] == b[j]:
    #                 dp[i][j] = 1 +  dp[i+1][j+1]
    #             else:
    #                 dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    #     return dp[0][0]

    def longestPalindromeSubseq(self, s: str) -> int:
        # we can check pallidrome by expanding
        # from left and right and see how long pallidrome
        # string can be made
        cache = {}

        def dfs(i, j):
            # edge case if left and right pointer reach boundary
            if i < 0 or j >= len(s):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == s[j]:
                # now we can have two scenerio, either odd length
                # or even length, in odd length both pointer will be
                # on same position, so we need to keep track
                length = 1 if i == j else 2 
                cache[(i,j)] = length + dfs(i-1, j+1)
            else:
                # we need to move both ways
                cache[(i,j)] = max(dfs(i-1, j), dfs(i, j+1))
            
            return cache[(i,j)]
        
        # now we need to check pallidrome at each index
        for i in range(len(s)):
            dfs(i, i) # odd length
            dfs(i, i+1) # even length
        
        return max(cache.values())
