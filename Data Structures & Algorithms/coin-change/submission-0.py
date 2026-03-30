class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we can compute first the no of coins required for amount
        # = 0 that is 0, now for amount 1 : 1 + dp[0] simillary
        # however we have to find minimum coin so we need to calculate
        # for others as well

        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[amount] if dp[amount] != amount + 1 else -1

