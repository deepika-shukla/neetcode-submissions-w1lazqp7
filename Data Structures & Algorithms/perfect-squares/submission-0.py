class Solution:

    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        # base case, for 0 target we need 0 square
        dp[0] = 0

        # traverse through all targets
        for target in range(1, n+1):
            # get all squares
            for s in range(1, target+1):
                square = s*s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[n]

