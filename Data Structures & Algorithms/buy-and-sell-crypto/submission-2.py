class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxx_profit = 0 
        for r in range(1, len(prices)):
            p = prices[r] - prices[l]
            if prices[l] > prices[r]:
                # that means we can buy at lowest price therefore changing l value
                prices[l] = prices[r]
            maxx_profit = max(maxx_profit, p)
        return maxx_profit

        