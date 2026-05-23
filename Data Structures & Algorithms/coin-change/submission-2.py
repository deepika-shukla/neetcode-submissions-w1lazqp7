class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        #edge case
        dp[0] = 0

        # compute for every sum
        for a in range(1, amount+1):
            for c in coins:
                # either there could be a coin with this amount
                # or we compute with diffrence of amount and coin
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount+1 else -1