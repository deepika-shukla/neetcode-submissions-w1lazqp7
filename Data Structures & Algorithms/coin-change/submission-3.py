class Solution:
    def coinChange(self, coins: List[int], amounts: int) -> int:
        dp = [amounts+1] * (amounts+1)
        dp[0] = 0

        for a in range(1, amounts+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amounts] if dp[amounts] != amounts+1 else -1