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
        memo = {}

        def dfs(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in memo:
                return memo[total]
            
            count = 0
            for num in nums:
                count += dfs(total+num)
            
            memo[total] = count
            return count
        
        return dfs(0)


        # dp
