class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days)+1)

        for i in reversed(range(len(days))):
            dp[i] = float("inf")
            j = i
            for d, c in zip([1,7,30], costs):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], dp[j] + c)
        return dp[0]