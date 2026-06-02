class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # recursive -- time limit will exceed as O(2^n)
        # we can either include profit or not

        # def helper(i, cap):
        #     if i == len(profit):
        #         return 0 
            
        #     # skip item i
        #     maxprofit = helper(i+1,cap)

        #     #include i
        #     newcap = cap - weight[i]
        #     if newcap >= 0:
        #         p = profit[i] + helper(i+1, newcap)
        #         maxprofit = max(maxprofit, p)
            
        #     return maxprofit
        
        # return helper(0,capacity)
            
        # memoization
        dp = [[-1] * (capacity+1) for _ in range(len(profit))]

        def helper(i, cap):
            if i == len(profit):
                return 0
            
            if dp[i][cap] != -1:
                return dp[i][cap]
            
            # skip item i
            dp[i][cap] = helper(i+1, cap)

            # include i
            newcap = cap - weight[i]
            if newcap >= 0:
                p = profit[i] + helper(i+1, newcap)
                dp[i][cap] = max(dp[i][cap], p)

            return dp[i][cap]
        return helper(0,capacity) 

