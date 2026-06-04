class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubseq(s, s[::-1])
    
    def longestCommonSubseq(self, a,b):
        dp = [[0]* (len(b)+1) for h in range(len(a) + 1) ]

        for i in range(len(a)-1,-1,-1):
            for j in range(len(b)-1,-1,-1):
                if a[i] == b[j]:
                    dp[i][j] = 1 +  dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
