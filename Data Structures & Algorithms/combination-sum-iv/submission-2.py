class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # recursive :  we need to try to include every number in nums
        
        # def dfs(total):
        #     if total == target:
        #         return 1
        #     if total > target:
        #         return 0
            
        #     count = 0
        #     for num in nums:
        #         count += dfs(num+total)

        #     return count
        
        # return dfs(0)


        # Memoization
        # we can store the count for particular sum
        # memo = {}

        # def dfs(total):
        #     if total == target:
        #         return 1
        #     if total > target:
        #         return 0
        #     if total in memo:
        #         return memo[total]
            
        #     count = 0
        #     for num in nums:
        #         count += dfs(total+num)
            
        #     memo[total] = count
        #     return count
        
        # return dfs(0)


        # dp
        dp = {0:1}
        # we need to caclucate for each target, like target is 4
        # what are number of ways to get sum 3, 2, 1.
        # for 0 we took the base case

        for i in range(1, target+1):
            dp[i] = 0 # for now
            for n in nums:
                dp[i] += dp.get(i-n, 0)
        return dp[target]

        
