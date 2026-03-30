class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to find max profit
        # we know we cannot go back in time
        # also we will purchase at least price and sell at higher
        # try to find the least, if you find smaller than that update
        # and calculate the diff, if the diff goes in negative keep it zero
        # otherwise keep it highest positive

        profit = 0 
        least = prices[0]

        for i in range(1, len(prices)):
            diff = prices[i] - least
            if diff > profit:
                profit = diff
            if prices[i] < least:
                least = prices[i]
        return profit

